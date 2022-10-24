package b2c_dto;

import java.sql.Date;

import b2c_dto.UserDTO.UserType;

public class ProductDTO {
	//product가 갖는 속성 : prodNum int, pname var, kind var,
	//price int, content var, useyn var, regdate date
	
	public enum UseYN{
		Y("상품 주문이 가능한 제품입니다. :) "),
		N("재고소진 상태 입니다. 재입고를 기다려주세요. :) ")
	    ;
	  	
	  	//파이널 필드를 생성해 라벨 값 생성.
	    private final String label;

	    UseYN(String label) {
	        this.label = label;
	    }

	    public String label() {
	        return label;
	    }} 
	
	private int prodNum; // 상품 등록시 자동 ++
	private String sellerId; // 판매자
	private String pname; // 상품 이름
	private String kind; // 상품 종류
	private int price; // 상품 가격
	private String content; // 상품 설명
	private UseYN useyn; // 상품 재고 유무
	private String regdate; // 상품 등록 날짜
	
	public ProductDTO() {};
	
	public ProductDTO(String sellerId, String pname, String kind, int price, String content) {
		this.sellerId = sellerId;
		this.pname = pname; 
		this.kind = kind;  
		this.price = price;
		this.content = content;
	
	}
	
	// 모든 물품 목록 받아오는 메소드
	public ProductDTO(int int1, String string, String string2, String string3, int int2, String string4, String string5,
			String string6) {
		this.prodNum = int1;
		this.sellerId = string;
		this.pname = string2;
		this.kind = string3;
		this.price = int2;
		this.content = string4;
		this.regdate = string6;
		
		switch(string5) {
	      case "Y":
	        this.useyn = UseYN.Y;
	        break;
	      case "N":
	        this.useyn = UseYN.N;
	        break;
	      case "재고소진 상태 입니다. 재입고를 기다려주세요. :) " :
	    	this.useyn = UseYN.N;
	    	break;
	      case "null":
	    	this.useyn = UseYN.Y;
	    	break;
	      default:
	        this.useyn = UseYN.Y;
	        break;
	    }
		
	}

	public String getSellerId() {
		return sellerId;
	}

	public void setSellerId(String sellerId) {
		this.sellerId = sellerId;
	}

	public int getProdNum() {
		return prodNum;
	}

	public void setProdNum(int prodNum) {
		this.prodNum = prodNum;
	}

	public String getPname() {
		return pname;
	}

	public void setPname(String pname) {
		this.pname = pname;
	}

	public String getKind() {
		return kind;
	}

	public void setKind(String kind) {
		this.kind = kind;
	}

	public int getPrice() {
		return price;
	}

	public void setPrice(int price) {
		this.price = price;
	}

	public String getContent() {
		return content;
	}

	public void setContent(String content) {
		this.content = content;
	}

	public UseYN getUseyn() {
		return useyn;
	}

	public void setUseyn(UseYN useyn) {
		this.useyn = useyn;
	}

	public String getRegdate() {
		return regdate;
	}

	public void setRegdate(String regdate) {
		this.regdate = regdate;
	}

	@Override
	public String toString() {
		return "상품 정보 [ 상품번호  = " + prodNum + ", 판매자  = " + sellerId + ", 상품이름 = " + pname + ", 상품종류 = " + kind + ", 금액 = " + price
				+ ", 상품 설명 = " + content + ", 주문 가능 여부 = " + useyn.label() + ", 상품 등록 날짜 = " + regdate + " ]";
	}
	
	
	
	
}
