<!doctype html>
<html lang="en">
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link href="https://fonts.googleapis.com/css2?family=Single+Day&display=swap" rel="stylesheet">
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <title>스파르타코딩클럽 | 부트스트랩 연습하기</title>
    <style>
        .wrap {
            width: 500px;
            margin: 10px auto;
        }
        .myimage {
            width: 500px;
            height: 300px;
        }
        .submitButton{
        margin: auto;
        width: 20%;
        }
    </style>
</head>
<body>
    <div class="wrap">
        <img class="myimage" src="https://i.ytimg.com/vi/8kXlxB8owGk/maxresdefault.jpg">
        <br>
        <h5>이 양초는 사실 특별한 힘을 가지고 있어요. 양초를 키고 소원을 빌면 짜자잔 뭐든지 이뤄지게 된답니다. 하나 사가세요! 대나무 향이 아주 좋아요.</h5>
         <!-- 달러 원환율 추가 -->
       <hd>
        <span style="color:blue"> 달러-원 환율 :</span>
        <span id="rate" style="color:blue"></span>
        </hd>
       <br>
        <div class="input-group mb-3">
            <div class="input-group-prepend">
                <button type="button">주문자이름</button>
            </div>
            <input type="text" class="form-control" placeholder="" aria-label="" aria-describedby="basic-addon1">
        </div>
        <div class="input-group mb-3">
            <div class="input-group-prepend">
                <button type="button">수량</button>
            </div>
            <select class="custom-select" id="inputGroupSelect03">
                <option value="1">--수량을 선택하세요 --</option>
                <option value="2">1</option>
                <option value="3">2</option>
                <option value="3">3</option>
                <option value="3">4</option>
                <option value="3">5</option>
            </select>
        </div>
        <div class="input-group mb-3">
            <div class="input-group-prepend">
                <button type="button">주소</button>
            </div>
            <input type="text" class="form-control" placeholder="" aria-label="" aria-describedby="basic-addon1">
        </div>
        <div class="input-group mb-3">
            <div class="input-group-prepend">
                <button type="button">전화번호</button>
            </div>
            <input type="text" class="form-control" placeholder="" aria-label="" aria-describedby="basic-addon1">
        </div>
        <div class="submitButton">
        <button class="btn btn-primary" type="submit">주문하기</button>
        </div>
    </div>
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
    integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
    crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
    integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
    crossorigin="anonymous"></script>
    <script>
        $(document).ready(function(){
            alert('다 로딩됐다!')
            // 여기에 환율 API Ajax 요청을 하면 되겠죠?
            $.ajax({
                type: "GET", // GET 방식으로 요청한다.
                url: "https://api.manana.kr/exchange/rate.json",
                data: {}, // 요청하면서 함께 줄 데이터 (GET 요청시엔 비워두세요)
                success: function(response){ // 서버에서 준 결과를 response라는 변수에 담음
                    console.log(response) // 서버에서 준 결과를 이용해서 나머지 코드를 작성
                    alert('Ajax 완료')
                    let rate = response[1]["rate"];
                    document.all("rate").innerHTML= rate //rate = 1229.45
                }
            })
        });
    </script>
    <!-- 
    -->
</body>
</html>