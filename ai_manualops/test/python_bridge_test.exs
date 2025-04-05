defmodule AiManualops.PythonBridgeTest do
  use ExUnit.Case
  alias AiManualops.PythonBridge

  setup do
    # 테스트가 시작될 때 Python 브릿지가 실행 중인지 확인
    :timer.sleep(100) # 브릿지 시작을 위한 짧은 대기
    :ok
  end

  test "echo handler" do
    message = "Hello, Python!"
    assert {:ok, ^message} = PythonBridge.echo(message)
  end

  test "sum handler" do
    numbers = [1, 2, 3, 4, 5]
    assert {:ok, 15} = PythonBridge.sum(numbers)
  end

  test "process data handler" do
    data = %{"name" => "test", "value" => 42}
    assert {:ok, result} = PythonBridge.process_data(data)
    assert result["received"] == data
    assert result["length"] == 2
    assert result["keys"] == ["name", "value"]
  end

  test "list manipulation handler - reverse" do
    items = [1, 2, 3, 4, 5]
    assert {:ok, [5, 4, 3, 2, 1]} = PythonBridge.list_manipulation(items, "reverse")
  end

  test "list manipulation handler - sort" do
    items = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert {:ok, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]} = PythonBridge.list_manipulation(items, "sort")
  end

  test "list manipulation handler - unique" do
    items = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    assert {:ok, result} = PythonBridge.list_manipulation(items, "unique")
    assert Enum.sort(result) == [1, 2, 3, 4]
  end

  test "list manipulation handler - invalid operation" do
    items = [1, 2, 3]
    assert {:error, _} = PythonBridge.list_manipulation(items, "invalid_op")
  end
end
