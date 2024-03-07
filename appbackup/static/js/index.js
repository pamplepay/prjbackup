$(document).ready(function() {
    // 동적으로 추가되는 요소에 대해 이벤트 위임 사용
    $('body').on('input', 'input[data-type="currency"]', function() {
        // 숫자 외의 모든 문자 제거
        var value = $(this).val().replace(/,/g, '').replace(/[^\d]/g, '');
        // 3자리마다 콤마 추가
        $(this).val(value.replace(/\B(?=(\d{3})+(?!\d))/g, ","));
    });

    $('body').on('input', '#businessNumber', function() {
        var input = $(this).val();
        var formattedInput = input.replace(/[^0-9\-]/g, '').replace(/^(\d{3})(\d{2})(\d{5})$/, '$1-$2-$3');
        $(this).val(formattedInput);
    });

    $('body').on('input', '#contact', function() {
        var input = $(this).val();
        var formattedInput = input.replace(/[^0-9\-]/g, '').replace(/^(\d{3})(\d{4})(\d{4})$/, '$1-$2-$3');
        $(this).val(formattedInput);
    });

    // "추가" 버튼 클릭 이벤트 핸들러
    $(".btnadd").click(function() {
        console.log(regions)
        $.ajax({
            url: 'dialog_add/', // Django 뷰의 URL을 지정하세요.
            type: 'GET',
            success: function(response) {
                $("#addPharmacyModal .modal-body").html(response);
                // index.html의 파트 선택 목록을 dialog_add.html의 파트 선택 목록으로 복사
                var selpartsOptions = $("#selparts").html();
                $("#addPharmacyModal #parts").html(selpartsOptions);
                // index.html에서 현재 선택된 파트를 dialog_add.html의 파트 선택 목록에서도 선택
                $("#addPharmacyModal #parts").val(selectedPartId);
                $("#addPharmacyModal").modal("show");

                var selectedPartId = $("#selparts").val();
                // regions 변수 파싱 (이미 페이지에 정의된 경우)
                   
                var $regionSelect = $("#addPharmacyModal #region");
                // 기존 옵션 제거
                $regionSelect.empty();

                // regions 객체를 순회하며 <option> 태그 생성 및 추가
                regions.forEach(function(region) {
                    var option = new Option(region.name, region.id);
                    $regionSelect.append($(option));
                });
            }
        });
    });

    $("#savePharmacy").click(function() {
        var formData = $("#addPharmacyForm").serialize(); // 폼 데이터 직렬화
        $.ajax({
            type: "POST",
            url: 'save_pharmacy/',
            data: formData,
            success: function(response) {
                // 성공 처리 로직
                console.log("Data saved successfully");
                $("#addPharmacyModal").modal('hide'); // 모달 숨기기
            },
            error: function(xhr, status, error) {
                // 오류 처리 로직
                console.error("Error saving data: " + error);
            }
        });
    });
});
