package b2c_dto;

import java.sql.Date;
//orderNum int , order_id var, total_price , indate date,
//result var 

import b2c_dto.UserDTO.UserType;

public class OrderDTO{
	// order가 갖는 속성 : ordernum, order_id, total_price, indete, result
   
	public enum Result{
		W("배송 전 입니다."),
	    S("배송이 시작 되었습니다."),
		C("배송이 완료 되었습니다.");
	    ;
	  	
	  	//파이널 필드를 생성해 라벨 값 생성.
	    private final String label;

	    Result(String label) {
	        this.label = label;
	    }

	    public String label() {
	        return label;
	    }} 
	
	private int orderNum; // 주문 번호  
	private String orderId;  // 주문자
	private String indate; // 주문한 날짜
	private Result result; // 배송 현황
   
	public OrderDTO() {}

	public OrderDTO(String orderId) {
      this.orderId = orderId;
   }


public OrderDTO(int int1, String string, String string2, String string3) {
	this.orderNum = int1;
	this.orderId = string;
	this.indate = string2;
	switch(string3) {
    case "W":
      this.result = Result.W;
      break;
    case "S":
      this.result = Result.S;
      break;
    case "C" :
  	this.result = Result.C;
  	break;
    case "배송이 시작 되었습니다." :
    this.result = Result.S;
    break;
    case "배송이 완료 되었습니다." :
    this.result = Result.C;
    break;
    case "null":
  	this.result = Result.W;
  	break;
    default:
      this.result = Result.W;
      break;
  }
	}

public int getOrderNum() {
      return orderNum;
   }

   public String getOrderId() {
      return orderId;
   }

   public void setOrderId(String orderId) {
      this.orderId = orderId;
   }


   public String getIndate() {
      return indate;
   }

   public void setIndate(String indate) {
      this.indate = indate;
   }

   public Result getResult() {
      return result;
   }

   public void setResult(Result result) {
      this.result = result;
   }

   @Override
   public String toString() {
      return "주문목록 [ 주문번호 = " + orderNum + ", 주문자 아이디 = " + orderId +  ", 주문 날짜 = "
            + indate + ", 배송 현황 = " + result.label() + " ]";
   }
}