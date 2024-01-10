public interface ActorBehavior {
    void setMakeOrder(boolean make);
    void setTakeOrder(boolean take);
    boolean isMakeOrder();
    boolean isTakeOrder();
}
