package service;

import java.sql.SQLException;
import java.util.ArrayList;

import b2c_dto.CartDTO;
import b2c_dto.MyDTO;
import b2c_dto.OrderDTO;
import b2c_dto.OrderDetailDTO;
import b2c_dto.ProductDTO;
import b2c_dto.UserDTO;
import b2c_dto.OrderDTO.Result;
import dao.CartDAO;
import dao.MyDAO;
import dao.OrderDAO;
import dao.OrderDetailDAO;
import dao.ProductDAO;
import dao.UserDao;
import view.B2CEndView;

public class Service {

	private static Service instance = new Service();
	
	private Service() {}
	
	public static Service getInstance() {
		return instance;
	}
	
// ---------------------- 회원 관련 서비스 ------------
	// 새로운 USER 회원가입
	public void addUser(UserDTO newuser) {
		try {
			UserDao.insertUser(newuser);
			// 회원가입에 성공한 경우 메세지 출력
			System.out.println("회원가입에 성공하셨습니다.");
		} catch (SQLException e) {
			e.printStackTrace();
			// PK(아이디)값이 이미 존재하는 경우 에러 메세지 출력
			B2CEndView.showError("존재하는 아이디 입니다. 다시입력 해 주세요");
		}
	}
	
	
	// 모든 회원 정보 반환
	public ArrayList<UserDTO> getAllUser() throws SQLException{
		return UserDao.getAllUsers();
	}
	
	
	// 회원 비밀번호 변경
	public void updateUserPw(String id, String pw, String ssn, String nextpw) throws SQLException{
		ArrayList<UserDTO> pwUser = UserDao.getAllUsers();
		for (int i = 0; i<pwUser.size() ; i++) {
			if (pwUser.get(i).getId().equals(id)) {
				if (pwUser.get(i).getPw().equals(pw)) {
					if (pwUser.get(i).getSsn().equals(ssn)) {
						UserDao.updatePw(id, pw, ssn, nextpw);
					}
				}
			}
		}
	}
	
	
	// 회원 주소지 변경
	public void updateUserAddress(String id, String pw, String ssn, String newaddress) throws SQLException{
		ArrayList<UserDTO> pwUser = UserDao.getAllUsers();
		for (int i = 0; i<pwUser.size() ; i++) {
			if (pwUser.get(i).getId().equals(id)) {
				if (pwUser.get(i).getPw().equals(pw)) {
					if (pwUser.get(i).getSsn().equals(ssn)) {
						UserDao.updateAddress(id, pw, ssn, newaddress);
					}
				}
			}
		}
	}
	
	
	// 판매자 계정으로 변환
	public void updateUser(String id, String pw, String ssn, String business_number) throws SQLException{
		ArrayList<UserDTO> pwUser = UserDao.getAllUsers();
		for (int i = 0; i<pwUser.size() ; i++) {
			if (pwUser.get(i).getId().equals(id)) {
				if (pwUser.get(i).getPw().equals(pw)) {
					if (pwUser.get(i).getSsn().equals(ssn)) {
						try {
							UserDao.updateUser(id, pw, ssn, business_number);
						} catch (SQLException e) {
							e.printStackTrace();
							B2CEndView.showError("정보가 잘못 입력되었습니다. 다시 시도해 주세요");
						}
					}
				}
			}
		}
	}
	
	
	// 회원 search
	public UserDTO searchUser(String id) throws SQLException{
		ArrayList<UserDTO> pwUser = UserDao.getAllUsers();
		for (int i = 0; i<pwUser.size() ; i++) {
			if (pwUser.get(i).getId().equals(id)) {
				return pwUser.get(i);
			}					
	}
		return null;
		
		
		
	
	}
	
	
	// 회원 탈퇴  - > 입력 한 아이디와 비밀번호, 주민등록번호를 비교해 사용자 인증 후 탈퇴
	public void deleteUser(String id, String pw, String ssn) throws SQLException{
		ArrayList<UserDTO> pwUser = UserDao.getAllUsers();
		for (int i = 0; i<pwUser.size() ; i++) {
			if (pwUser.get(i).getId().equals(id)) {
				if (pwUser.get(i).getPw().equals(pw)) {
					if (pwUser.get(i).getSsn().equals(ssn)) {
						try {
							UserDao.deleteUser(id);
						} catch (SQLException e) {
							e.printStackTrace();
							B2CEndView.showError("정보가 잘못 입력되었습니다. 다시 시도해 주세요");
						}
					}
				}
			}
		}
	}
	
	
	
//	------------------------로그인 -------------------------------
	
	// 로그인 서비스
	public void logIn() throws SQLException {
		MyDTO my = new MyDTO();
		my.memberLoginEx();
		ArrayList<UserDTO> pwUser = UserDao.getAllUsers();
		for (int i = 0; i<pwUser.size() ; i++) {
			if (pwUser.get(i).getId().equals(my.getId())) {
				if (pwUser.get(i).getPw().equals(my.getPw())) {
					try {
						MyDAO.logIn(my.getId(),my.getPw());
					} catch (SQLException e) {
						e.printStackTrace();
						B2CEndView.showError("정보가 잘못 입력되었습니다. 다시 시도해 주세요");
					}
				}
			}
		}
	}
	
//--------------------------물품 관련 서비스 -------------------	
	
	
	// 물품 등록
	public void addProduct(ProductDTO newuser) throws SQLException {
		ProductDAO.insertProduct(newuser);
	}
	
	
	// 물품 금액 변경
	public boolean updateProductPrice(String id, String pw, String ssn,int prodNum, Double newprice) throws Exception {
		ArrayList<UserDTO> product = UserDao.getAllUsers();
		for (int i = 0; i<product.size() ; i++) {
			if (product.get(i).getId().equals(id)) {
				if (product.get(i).getPw().equals(pw)) {
					if (product.get(i).getSsn().equals(ssn)) {
						try {
							ProductDAO.updateProductPrice(id, prodNum, newprice);
							return true;
						} catch (SQLException e) {
							e.printStackTrace();
							B2CEndView.showError("정보가 잘못 입력되었습니다. 다시 시도해 주세요");
						}
					}
				}
			}
		}
		return false;
	}
	
	
	
	// 재고현황 변경
	public boolean updateProductYN(String id, String pw, String ssn,int prodNum, String useyn) throws Exception {
		ArrayList<UserDTO> product = UserDao.getAllUsers();
		for (int i = 0; i<product.size() ; i++) {
			if (product.get(i).getId().equals(id)) {
				if (product.get(i).getPw().equals(pw)) {
					if (product.get(i).getSsn().equals(ssn)) {
						try {
							ProductDAO.updateProductYN(id, prodNum, useyn);
							return true;
						} catch (SQLException e) {
							e.printStackTrace();
						}
					}
				}
			}
		}
		return false;
	}
	
	
	// 모든 물품 정보 반환
	public ArrayList<ProductDTO> getAllProduct() throws SQLException{
		return ProductDAO.getAllProduct();
	}
	
	
	// 판매자 아이디를 검색해 동일한 판매자의 아이템 리스트 출력
	public ArrayList<ProductDTO> searchProductId(String id) throws Exception {
		return ProductDAO.searchProductId(id);
	}
	
	// 상품 명을 검색해 아이템 리스트 출력
	public ArrayList<ProductDTO> searchProductPname(String pname) throws Exception {
		return ProductDAO.searchProductPname(pname);
	}
	
	
	// 상품 명을 검색해 아이템 리스트 출력
	public ArrayList<ProductDTO> searchProductKind(String kind) throws Exception {
		return ProductDAO.searchProductKind(kind);
	}
	
	
	// 상품삭제 - 개인정보 인증이 완료되면 입력한 상품 번호 삭제 
	public void deleteProduct(String id, String pw, String ssn, int prodNum) throws SQLException{
		ArrayList<UserDTO> pwUser = UserDao.getAllUsers();
		for (int i = 0; i<pwUser.size() ; i++) {
			if (pwUser.get(i).getId().equals(id)) {
				if (pwUser.get(i).getPw().equals(pw)) {
					if (pwUser.get(i).getSsn().equals(ssn)) {
						try {
							ProductDAO.deleteUser(id, prodNum);
						} catch (SQLException e) {
							e.printStackTrace();
							B2CEndView.showError("정보가 잘못 입력되었습니다. 다시 시도해 주세요");
						}
					}
				}
			}
		}
	}
	
//	-----------------------------Cart 서비스 -------------------------
	
	// 장바구니 목록에  추가
	public void addCart(CartDTO newcart) throws SQLException {
		CartDAO.insertCart(newcart);
	}
	
	
	// 나의 장바구니 목록 불러오기
	public ArrayList<CartDTO> searchMyCart(String id) throws SQLException{
		ArrayList<UserDTO> cart = UserDao.getAllUsers();
		for (int i = 0; i<cart.size() ; i++) {
			if (cart.get(i).getId().equals(id)) {
				return CartDAO.getCart(id);
			}					
	}
		return null;
	}
	
	
	// 장바구니 내 아이템 삭제하기
	public boolean deleteProductCart(String id, int cartNum) throws SQLException{
		ArrayList<UserDTO> cart = UserDao.getAllUsers();
		for (int i = 0; i<cart.size() ; i++) {
			if (cart.get(i).getId().equals(id)) {
				return CartDAO.deleteProductCart(id, cartNum);
			}					
	}
		return false;
	}
	
	
	// 장바구니 내 아이템 수정하기
	public boolean updateProductCart(String id, int prodnum, int cartNum, int num) throws SQLException{
		ArrayList<UserDTO> cart = UserDao.getAllUsers();
		for (int i = 0; i<cart.size() ; i++) {
			if (cart.get(i).getId().equals(id)) {
				return CartDAO.updateProductCart(id,prodnum, cartNum,num);
			}					
	}
		return false;
	}
	
	
	// 장바구니의 총 금액 계산해주기
	public int sumCart(String id) throws SQLException{
		ArrayList<UserDTO> cart = UserDao.getAllUsers();
		for (int i = 0; i<cart.size() ; i++) {
			if (cart.get(i).getId().equals(id)) {
				return CartDAO.sumCart(id);
			}					
	}
		return 0;
		
	}
	
	
// ----------------------------주문 테이블 -----------------------------
	
	
	// 주문 테이블 생성
	public void addOrder(OrderDTO neworder) throws SQLException {
		ArrayList<UserDTO> order = UserDao.getAllUsers();
		for (int i = 0; i<order.size() ; i++) {
			if (order.get(i).getId().equals(neworder.getOrderId())) {
				OrderDAO.addOrder(neworder);
			}}
	}
		
		
	// 주문 상세 테이블 생성 - 장바구니에서 그대로 삽입
	public void insertOrderDetail(String id) throws SQLException {
		ArrayList<UserDTO> order = UserDao.getAllUsers();
		for (int i = 0; i<order.size() ; i++) {
			if (order.get(i).getId().equals(id)) {
				OrderDetailDAO.insertOrderDetail(id);
			}
	}
		
	}
	
	
	// 주문 번호 붙여주기
	public void updateOrderDetail(String id) throws SQLException {
		ArrayList<UserDTO> order = UserDao.getAllUsers();
		for (int i = 0; i<order.size() ; i++) {
			if (order.get(i).getId().equals(id)) {
				OrderDetailDAO.updateOrderDetail(id);
			}
		}
	}
	
	
	//주문 정보 불러오기
	public ArrayList<OrderDTO> searchOrder(String id) throws SQLException {
		ArrayList<UserDTO> order = UserDao.getAllUsers();
		for (int i = 0; i<order.size() ; i++) {
			if (order.get(i).getId().equals(id)) {
				return OrderDAO.searchOrder(id);
			}
		}
		return null;
	}
	
	//// 주문 번호로 검색한 정보 불러오기
	public ArrayList<OrderDTO> searchOrdernum(int ordernum) throws SQLException {
			 return OrderDAO.searchOrdernum(ordernum);
	}
	
	////주문 번호로 검색한 정보 불러오기
	public ArrayList<OrderDetailDTO> searchOrderDetailnum(int ordernum) throws SQLException {
			 return OrderDetailDAO.searchOrderDetailnum(ordernum);
	}
	
	
	
	// 주문 상세정보의 총 합 구해주기
	public int sumOrderDetail(int ordernum) throws SQLException{
			return OrderDetailDAO.sumOrderDetail(ordernum);
	
	}
	
	// 배송 현황 변경
	// 주문 상세정보의 총 합 구해주기
	public boolean updateOrder(int ordernum,String result) throws SQLException{
			return OrderDAO.updateOrder(ordernum, result);
	
	}
}