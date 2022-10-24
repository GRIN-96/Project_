package dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

import b2c_dto.CartDTO;
import b2c_dto.UserDTO;
import dbutil.DBUtil;

public class CartDAO {



//DAO : DB와 연동해 데이터를 입력, 수정, 삭제 등을 수행하는 클래스. 여기서 본격적인 SQL 쿼리가 수행됨.
	// Insert, Update, Delete methods ...
	
	//1. 장바구니에 상품을 추가하는 메소드
	  public static boolean insertCart(CartDTO cart) throws SQLException {

	    Connection con = null; // Connection :: DB와 JAVA를 연결시켜주는 역할을 하는 객체이다.
	    PreparedStatement pstmt = null; // PreparedStatement :: SQL문을 실행할 때 실행을 위한 SQL을 DB에 전달하는 역할을 수행하는 객체다.
	     System.out.println("장바구니에 상품을 담는 중입니다.");
	     
	    //order_id, prodnum, pname, price, quantity
	    try {

	      //1. DB 연결
	      con = DBUtil.getConnection();
	      pstmt = con.prepareStatement("insert into cart (order_id, prodnum, pname, price, quantity) values(?, ?, (select pname from product where prodnum = ?), (select price from product where prodnum = ?), ?);"); // '?'는 아직 값이 정해지지 않은 SQL문의 변수를 의미한다.

	      //2. SQL Query 완성
	        // .setString()을 사용하여 각각의 ?위치에 값을 String으로 입력한다. (index, value)순서
	      pstmt.setString(1, cart.getOrderId());
	      pstmt.setInt(2, cart.getProdnum());
	      pstmt.setInt(3, cart.getProdnum());
	      pstmt.setInt(4, cart.getProdnum());
	      pstmt.setInt(5, cart.getQuantity());
	      
	      
	      
	      //3. Query 실행
	      int result = pstmt.executeUpdate(); //.executeUpdate() :: Compile된 DML문을 실행시킴. 성공적으로 수행된 경우 1, 실패한 경우 0 을 반환한다.
	      if (result == 1) {
	        return true;
	      } 
	    } finally {
	    	System.out.println("성공적으로 작업이 이루어졌습니다.");
	      DBUtil.close(con, pstmt); //DB connection 종료
	    } return false;
	  }
	  
	  
	//2. 나의 장바구니 정보를 모두 가져오는 메소드
	public static ArrayList<CartDTO> getCart(String id) throws SQLException {
	Connection con = null;
	PreparedStatement pstmt = null;
	ResultSet rs = null;  //ResultSet :: select 문을 실행했을 경우 데이터베이스에서 결과를 받아와 저장하는 객체이다.
	ArrayList<CartDTO> list = new ArrayList<CartDTO>(); //반환할 모든 Seller객체 정보를 담을 ArrayList 생성
	try {
	  con = DBUtil.getConnection();
	  pstmt = con.prepareStatement("SELECT * FROM cart WHERE order_id =?");
	  pstmt.setString(1, id);
	  
	  rs = pstmt.executeQuery();
	  while (rs.next()) { // .next() : 수행결과로 ResultSet객체에서 하나의 Row를 반환한다. 더이상 결과가 없을 경우 false를 반환하면서 리턴
	                      // next()메소드를 한번 호출할때마다 한개의 레코드를 아이템으로 가진 객체를 반환한다.
	
		  CartDTO user = new CartDTO(
    		rs.getInt("cartNum"), //ResultSet에서 getString()을 사용하여 각각의 컬럼의 값을 가져온다.
            rs.getString("order_id"),
            rs.getInt("prodnum"),
            rs.getString("pname"),
            rs.getInt("price"),
            rs.getInt("quantity")
        );
	    list.add(user); //각 User객체를 ArrayList에 추가
	  }
	} finally {
	  DBUtil.close(con, pstmt, rs);
	} return list;
	}
	
	
	//3. 장바구니내 물건 삭제
	public static boolean deleteProductCart(String id, int cartNum) throws SQLException {
	    Connection con = null;
	    PreparedStatement pstmt = null;
	    System.out.println("장바구니 내 상품 삭제를 진행 중입니다.");
	    try {
	      con = DBUtil.getConnection();
	      pstmt = con.prepareStatement("DELETE FROM cart WHERE order_id = ? and cartNum =? ");
	      pstmt.setString(1, id);
	      pstmt.setInt(2, cartNum);
	      int result = pstmt.executeUpdate();
	      if (result == 1) {
	    	 System.out.println("상품이 삭제되었습니다.");
	        return true;
	      }
	    } finally {
	      DBUtil.close(con, pstmt);
	    } return false;
	  }
	
	
	
	//4 . 장바구니 물건 수량 수정
	public static boolean updateProductCart(String id, int prodnum, int cartNum, int num) throws SQLException {
	    Connection con = null;
	    PreparedStatement pstmt = null;
	    System.out.println("장바구니 내 상품 수량 수정을 진행 중입니다.");
	    try {
	      con = DBUtil.getConnection();
	      pstmt = con.prepareStatement("UPDATE cart SET quantity = ? WHERE order_id =? AND prodnum =? AND cartNum =? ");
	      pstmt.setInt(1, num);
	      pstmt.setString(2, id);
	      pstmt.setInt(3, prodnum);
	      pstmt.setInt(4, cartNum);
	      int result = pstmt.executeUpdate();
	      if (result == 1) {
	    	 System.out.println("수정이 완료되었습니다.");
	        return true;
	      }
	    } finally {
	      DBUtil.close(con, pstmt);
	    } return false;
	  }
	
	
	
	// 5. 장바구니내 총 금액 계산
	public static int sumCart(String id) throws SQLException {
	    Connection con = null;
	    PreparedStatement pstmt = null;
	    ResultSet rs = null;
	    int list = 0;
	    System.out.println("계산중입니다.");
	    try {
	      con = DBUtil.getConnection();
	      pstmt = con.prepareStatement("select sum(quantity * price) from order_detail where order_id = ? ");
	      pstmt.setString(1, id);
	      
	      rs = pstmt.executeQuery();
	      while (rs.next()){
	    	  list = rs.getInt("sum(quantity * price)");

	      }
	    } finally {
	      DBUtil.close(con, pstmt, rs);
	    } 
		return list;
	  }
		
}
