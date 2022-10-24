package view;

import java.util.ArrayList;

import b2c_dto.CartDTO;
import b2c_dto.OrderDTO;
import b2c_dto.OrderDetailDTO;
import b2c_dto.ProductDTO;
import b2c_dto.UserDTO;

public class B2CEndView {

	//예외 상황 출력
	public static void showError(String message) {
		System.out.println(message);
	}
	
// ----------------------------- 회원 관련 서비스 -------------------------
	
	// 모든 회원의 정보를 출력
	public static void userView(ArrayList<UserDTO> allUser) {
		int length = allUser.size();
		if (length != 0) {
			for (int index = 0; index < length; index++) {
				System.out.println("검색정보" + (index + 1) + " - " + allUser.get(index));
			}
		}
	}
	
	
	
	// 검색 회원 정보 출력
	public static void searchUserView(UserDTO User) {
		System.out.println(User);
	}
	
	
	
//--------------------------물품 관련 정보 -------------------------
	
	//모든 물품 정보 불러오기
	public static void productView(ArrayList<ProductDTO> allproduct) {
		int length = allproduct.size();
		if (length != 0) {
			for (int index = 0; index < length; index++) {
				System.out.println("검색정보" + (index + 1) + " - " + allproduct.get(index));
			}
		}
	}
	
	
	// 검색 물품 정보 출력
	public static void searchProductView(ArrayList<ProductDTO> allproduct) {
		int length = allproduct.size();
		if (length != 0) {
			for (int index = 0; index < length; index++) {
				System.out.println("검색정보" + (index + 1) + " - " + allproduct.get(index));
			}
		}
	}

//-------------------------------장바구니 ---------------------------
	
	// 나의 장바구니 조회
	public static void searchMyCartView(ArrayList<CartDTO> allcart) {
		int length = allcart.size();
		if (length != 0) {
			for (int index = 0; index < length; index++) {
				System.out.println("검색정보" + (index + 1) + " - " + allcart.get(index));
			}
		}
	}
	
	
	//총 합 계산 출력
	public static void sumCash(int cash) {
		System.out.println(cash);
	}
	
	
//-----------------------------주문------------------------------------
	
	// 주문정보 조회
	public static void searchOrderView(ArrayList<OrderDTO> order) {
		int length = order.size();
		if (length != 0) {
			for (int index = 0; index < length; index++) {
				System.out.println("검색정보" + (index + 1) + " - " + order.get(index));
			}
		}
	}
	
	// 주문번호로 정보 조회
	
	// 주문정보 조회
	public static void searchOrderDetailView(ArrayList<OrderDetailDTO> order) {
		int length = order.size();
		if (length != 0) {
			for (int index = 0; index < length; index++) {
				System.out.println("검색정보" + (index + 1) + " - " + order.get(index));
			}
		}
	}
	
	
	// 주문 총합 금액
		public static void sumOrderDetailView(int cash) {
			System.out.println(cash);
		}

}
