function validate(log: string, actual: any, expectation: any): void {
  const result = actual === expectation ? "PASSED" : "FAILED";
  const message = ` [${log}] Result : ${result}, actual: ${actual}, expected: ${expectation}`;
  console.log(message);
}

interface bankMetadata {
  accountId: string;
  balance: number;
  timestamp: number;
  active: boolean;
}

interface paymentMetadata {
  accountId: string;
  amount: number;
  timestamp: number;
}

class BankStorage {
  private bankStorage: Map<string, bankMetadata[]>;
  private paymentStorage: Map<string, paymentMetadata[]>;

  constructor() {
    this.bankStorage = new Map();
    this.paymentStorage = new Map();
  }

  /**
   * Level 1: Basic Account Management
   */
  private _addNewPayment(accountId: string, amount: number, timestamp: number) : paymentMetadata {
    if (!this.paymentStorage.has(accountId)) {
        this.paymentStorage.set(accountId, [])
    }
    const metadata = {
        accountId, amount, timestamp
    }
    this.paymentStorage.set(accountId, [...this.paymentStorage.get(accountId) ?? [], metadata]) 
    return metadata;
  }
  private _deletePaymentBeforeTimestamp(accountId: string, ctimestamp: number) : paymentMetadata[] {
    let success = true;
    if (!this.paymentStorage.has(accountId)) {
        this.paymentStorage.set(accountId, [])
        success = false
    }
    const payments = this.paymentStorage.get(accountId) ?? [];
    payments.sort((a, b) => b.timestamp - a.timestamp);
    this.paymentStorage.set(accountId, [...payments.filter(m => m.timestamp > ctimestamp)]) 
    return payments.filter(m => m.timestamp <= ctimestamp);
  }
  private _createNewAccount(accountId: string): string | null {
    // account never added
    if (this.bankStorage.has(accountId)) {
      return null;
    }
    this.bankStorage.set(accountId, [
      ...this._getAccoutMetadatas(accountId),
      {
        accountId,
        balance: 0,
        timestamp: 0,
        active: true,
      },
    ]);
    return accountId;
  }
  private _getAccoutMetadatas(accountId: string): bankMetadata[] {
    const metadata = this.bankStorage.get(accountId);
    return metadata ?? [];
  }
  private _isAccountActive(accountId: string): boolean {
    const recentMetadata = this._getMostRecentBankMetadata(accountId);
    return recentMetadata == null ? false : recentMetadata.active;
  }
  private _getMostRecentBankMetadata(accountId: string): bankMetadata | null {
    const metadatas = this._getAccoutMetadatas(accountId);
    const metadata =
      metadatas.length > 0 ? metadatas[metadatas.length - 1] : null;
    return metadata;
  }
  private _getAccoutMetadataAtTimestamp(
    accountId: string,
    timestamp: number,
  ): bankMetadata | null {
    const metadatas = this._getAccoutMetadatas(accountId);
    const metadataAtTimestamp = metadatas.findLast((metadata) => {
      return metadata.timestamp <= timestamp;
    });
    return metadataAtTimestamp ?? null;
  }
  private _updateAccout(
    accountId: string,
    balance: number,
    timestamp: number = 0,
    active: boolean = true,
  ): boolean {
    // account never added
    if (this.bankStorage.has(accountId)) {
      const recentMetadata = this._getMostRecentBankMetadata(accountId);
      this.bankStorage.set(accountId, [
        ...this._getAccoutMetadatas(accountId),
        {
          accountId,
          balance: balance,
          timestamp: timestamp && recentMetadata && timestamp > recentMetadata.timestamp ? timestamp : recentMetadata ? recentMetadata.timestamp : timestamp,
          active: active,
        },
      ]);
      return true
    }
    return false
  }
  private _deleteAccout(accountId: string): boolean {
    // account never added
    const recentMetadata = this._getMostRecentBankMetadata(accountId);
    return this._updateAccout(
      accountId,
      0,
      recentMetadata ? recentMetadata.timestamp + 1 : 0,
      false,
    );
  }

  // createAccount(account, balance) -> boolean
  // Fails if account already exists.
  createAccount(accountId: string, initialBalance: number): boolean {
    if (this._isAccountActive(accountId)) {
      return false;
    }
    const account = this._createNewAccount(accountId);
    this._updateAccout(accountId, initialBalance);
    return account ? true : false;
  }

  // getBalance(account) -> number | null
  // Returns current balance or null if account doesn't exist.
  // IMPORTANT: In a real system, you must process due payments before returning balance.
  getBalance(accountId: string, currentTimestamp?: number): number | null {
    if (!this._isAccountActive(accountId)) {
      return null;
    }
    if (currentTimestamp) {
        this.processPayments(currentTimestamp);
    }
    if (currentTimestamp) {
      const metadata = this._getAccoutMetadataAtTimestamp(
        accountId,
        currentTimestamp,
      );
      return metadata ? metadata.balance : null;
    }
    const recentMetadata = this._getMostRecentBankMetadata(accountId);
    return recentMetadata ? recentMetadata.balance : null;
  }

  // deleteAccount(account) -> boolean
  deleteAccount(accountId: string): boolean {
    // TODO: Remove account and potentially its pending payments
    return this._deleteAccout(accountId);
  }

  /**
   * Level 2: Transactions
   */

  // addAmountToAccount(account, amount) -> number | null
  // Adds (or subtracts) amount. Returns new balance.
  addAmountToAccount(accountId: string, amount: number, timestamp: number = 0): number | null {
    const currentBalance = this.getBalance(accountId);
    this._updateAccout(accountId, (currentBalance ? currentBalance + amount : amount), timestamp);
    // TODO: Update balance logic
    return this.getBalance(accountId) ?? null;
  }

  /**
   * Level 3: Analytics (Top N)
   */

  // getTopNAccountWithHighestBalance(n) -> string[]
  // Returns IDs of top N accounts. Sort by balance DESC, then ID ASC (lexicographical).
  getTopNAccountWithHighestBalance(n: number): string[] {
    const allBankMetadatas: bankMetadata[] = []
    this.bankStorage.forEach((metadatas) => {
        allBankMetadatas.push(metadatas[metadatas.length - 1])
    })
    allBankMetadatas.sort((a,b) => {
        const balanceComparison = b.balance - a.balance;
        if (balanceComparison != 0) {return balanceComparison}
        const userNameComparison = a.accountId.localeCompare(b.accountId);
        return userNameComparison
    })
    // TODO: Implement sorting logic
    return allBankMetadatas.filter((_, i) => {return i < n}).map((metadata) => {return metadata.accountId});
  }

  /**
   * Level 4: Scheduled Operations
   */

  // schedulePayment(timestamp, account, paymentAmount) -> boolean
  // Records a payment to be deducted at a future timestamp.
  schedulePayment(
    timestamp: number,
    accountId: string,
    amount: number,
  ): boolean {
    // TODO: Store payment and sort pendingPayments by timestamp
    this._addNewPayment(accountId, amount, timestamp)
    return true;
  }

  // A helper usually required to "tick" the system forward or
  // trigger payments before balance checks.
  processPayments(currentTimestamp: number): void {
    this.bankStorage.forEach((bankMetadatas, accountId) => {
        const payments = this._deletePaymentBeforeTimestamp(accountId, currentTimestamp);
        payments.forEach((payment, index) => {
            this.addAmountToAccount(accountId, -payment.amount, payment.timestamp)
        })
    })
    // TODO: Deduct amounts for all payments where payment.timestamp <= currentTimestamp
  }
}

const bank = new BankStorage();

// --- Level 1: Accounts ---
validate("Bank: Create User A", bank.createAccount("user_a", 100), true);
validate("Bank: Create Duplicate", bank.createAccount("user_a", 50), false);
validate("Bank: Get Balance", bank.getBalance("user_a"), 100);

// --- Level 2: Transactions ---
validate("Bank: Deposit", bank.addAmountToAccount("user_a", 50), 150);
validate("Bank: Withdraw", bank.addAmountToAccount("user_a", -20), 130);

// --- Level 3: Top N ---
bank.createAccount("user_c", 500);
bank.createAccount("user_d", 10);
bank.createAccount("user_b", 500);
// Expected: user_b and user_c are tied at 500.
// Tie-break: user_b comes before user_c alphabetically.
// Top 2 should be ["user_b", "user_c"]
validate("Bank: Top 2 Accounts", bank.getTopNAccountWithHighestBalance(2).join(""), [
  "user_b",
  "user_c",
].join(""));

// --- Level 4: Scheduled Payments ---
// Current balance user_b: 500. Schedule -100 at timestamp 1000.
validate(
  "Bank: Schedule Payment",
  bank.schedulePayment(1000, "user_b", 100),
  true,
);

// Check balance at T=500 (Payment shouldn't have happened yet)
validate("Bank: Balance before payment", bank.getBalance("user_b", 500), 500);

// Check balance at T=1001 (Payment should be processed)
validate("Bank: Balance after payment", bank.getBalance("user_b", 1001), 400);

// Edge Case: Insufficient funds at time of payment
bank.createAccount("user_e", 20);
bank.schedulePayment(2000, "user_e", 50); // Payment is more than balance
// Implementation choice: Does it go negative or fail? (Assume it goes negative for tests)
validate("Bank: Overdraft payment", bank.getBalance("user_e", 2001), -30);
