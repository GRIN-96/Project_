package b2c_dto;

public class CartDTO {
	//Orderdetail이 갖는 속성 :
	//ordernum int, order_id var, prodnum int, pname var, price int, 
	//quantity int, order_infomation int
	
	private int ordernum; // 상품 주문 종류 ( 몇개인지 체크용 )
	private String orderId; // 주문자
	private int prodnum; // 상품 번호
	private String pname; // 상품 이름
	private int price; // 상품 금액
	private int quantity; // 상품 구매개수 
	
	
	public CartDTO() {} // 생성자 함수
	
	public CartDTO(String orderId, int prodnum, int quantity) {
		this.orderId = orderId;
		this.prodnum = prodnum;
		this.quantity = quantity;
		
		
	}
	
	
	// 카트 모든 정보를 가져올 때 쓰는 함수
	public CartDTO(int int1, String string, int int2, String string2, int int3, int int4) {
		this.ordernum = int1;
		this.orderId = string;
		this.prodnum = int2;
		this.pname = string2;
		this.price = int3;
		this.quantity = int4;
	}

	public String getOrderId() {
		return orderId;
	}

	public void setOrderId(String orderId) {
		this.orderId = orderId;
	}

	public int getProdnum() {
		return prodnum;
	}

	public void setProdnum(int prodnum) {
		this.prodnum = prodnum;
	}

	public String getPname() {
		return pname;
	}

	public void setPname(String pname) {
		this.pname = pname;
	}

	public int getPrice() {
		return price;
	}

	public void setPrice(int price) {
		this.price = price;
	}

	public int getQuantity() {
		return quantity;
	}

	public void setQuantity(int quantity) {
		this.quantity = quantity;
	}

	@Override
	public String toString() {
		return "주문 상세정보 [카트 번호 = " + ordernum +", 주문자 = " + orderId + ", 상품 번호 = " + prodnum + ", 상품 이름 = " + pname + ", 상품금액 = " + price
				+ ", 상품 주문 개수 = " + quantity + "]";
	}

		
	}
	
	

