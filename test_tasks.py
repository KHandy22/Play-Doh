# test_tasks.py
import pytest
from unittest.mock import patch


# ==================================================================
# TASK 1 - Turtle build
# ==================================================================

@patch('builtins.input', side_effect=['big', 'option 1'])
def test_task1_color1_is_string_in_step1(mock_input, capsys):
    from task1 import main
    main()
    output = capsys.readouterr().out
    assert "1) Use " in output
    assert " to roll a medium-sized ball." in output


@patch('builtins.input', side_effect=['big', 'option 1'])
def test_task1_color1_is_string_in_step5(mock_input, capsys):
    from task1 import main
    main()
    output = capsys.readouterr().out
    assert "5) Use " in output
    assert " to roll a small ball." in output


@patch('builtins.input', side_effect=['big', 'option 1'])
def test_task1_color1_consistent_in_steps_1_and_5(mock_input, capsys):
    from task1 import main
    main()
    output = capsys.readouterr().out
    lines = output.split('\n')
    step1 = [line for line in lines if line.startswith("1) Use ")][0]
    step5 = [line for line in lines if line.startswith("5) Use ")][0]
    color_in_step1 = step1.replace("1) Use ", "").replace(" to roll a medium-sized ball.", "")
    color_in_step5 = step5.replace("5) Use ", "").replace(" to roll a small ball.", "")
    assert color_in_step1 == color_in_step5


@patch('builtins.input', side_effect=['big', 'option 1'])
def test_task1_input1_prompt_text(mock_input, capsys):
    from task1 import main
    main()
    assert mock_input.call_args_list[0][0][0] == "big or small? "


@patch('builtins.input', side_effect=['big', 'option 1'])
def test_task1_input2_prompt_text(mock_input, capsys):
    from task1 import main
    main()
    assert mock_input.call_args_list[1][0][0] == "option 1 or option 2? "


@patch('builtins.input', side_effect=['big', 'option 1'])
def test_task1_choice1_big(mock_input, capsys):
    from task1 import main
    main()
    output = capsys.readouterr().out
    assert "2) Flatten the ball into a wide disc." in output


@patch('builtins.input', side_effect=['small', 'option 1'])
def test_task1_choice1_small(mock_input, capsys):
    from task1 import main
    main()
    output = capsys.readouterr().out
    assert "2) Keep it as a ball." in output


@patch('builtins.input', side_effect=['big', 'option 1'])
def test_task1_choice2_option1(mock_input, capsys):
    from task1 import main
    main()
    output = capsys.readouterr().out
    assert "7) Pinch the small ball to make it pointy." in output


@patch('builtins.input', side_effect=['big', 'option 2'])
def test_task1_choice2_option2(mock_input, capsys):
    from task1 import main
    main()
    output = capsys.readouterr().out
    assert "7) Keep the small ball round." in output


# ==================================================================
# TASK 2 - Ladybug build
# ==================================================================

@patch('builtins.input', side_effect=['1', 'A', 'Ladybug'])
def test_task2_color2_is_string_in_step1(mock_input, capsys):
    from task2 import main
    main()
    output = capsys.readouterr().out
    assert "1) Use " in output
    assert " to roll a ball." in output


@patch('builtins.input', side_effect=['1', 'A', 'Ladybug'])
def test_task2_color2_is_string_in_step3(mock_input, capsys):
    from task2 import main
    main()
    output = capsys.readouterr().out
    assert "3) Use " in output
    assert " to roll two thin ropes." in output


@patch('builtins.input', side_effect=['1', 'A', 'Ladybug'])
def test_task2_color2_consistent_in_steps_1_and_3(mock_input, capsys):
    from task2 import main
    main()
    output = capsys.readouterr().out
    lines = output.split('\n')
    step1 = [line for line in lines if line.startswith("1) Use ")][0]
    step3 = [line for line in lines if line.startswith("3) Use ")][0]
    color_in_step1 = step1.replace("1) Use ", "").replace(" to roll a ball.", "")
    color_in_step3 = step3.replace("3) Use ", "").replace(" to roll two thin ropes.", "")
    assert color_in_step1 == color_in_step3


@patch('builtins.input', side_effect=['1', 'A', 'Ladybug'])
def test_task2_input1_prompt_text(mock_input, capsys):
    from task2 import main
    main()
    assert mock_input.call_args_list[0][0][0] == "1, 2, or 3? "


@patch('builtins.input', side_effect=['1', 'A', 'Ladybug'])
def test_task2_input2_prompt_text(mock_input, capsys):
    from task2 import main
    main()
    assert mock_input.call_args_list[1][0][0] == "A or B? "


@patch('builtins.input', side_effect=['1', 'A', 'Ladybug'])
def test_task2_input3_no_prompt(mock_input, capsys):
    from task2 import main
    main()
    assert mock_input.call_args_list[2][0] == ()


@patch('builtins.input', side_effect=['1', 'A', 'Ladybug'])
def test_task2_choice3_appears_in_namecard(mock_input, capsys):
    from task2 import main
    main()
    output = capsys.readouterr().out
    assert "Ladybug" in output
    assert "name card" in output


@patch('builtins.input', side_effect=['1', 'A', 'Butterfly'])
def test_task2_choice3_different_value_appears(mock_input, capsys):
    from task2 import main
    main()
    output = capsys.readouterr().out
    assert "Butterfly" in output


@patch('builtins.input', side_effect=['1', 'A', 'Ladybug'])
def test_task2_choice1_option1(mock_input, capsys):
    from task2 import main
    main()
    output = capsys.readouterr().out
    assert "2) Make the ball flat." in output


@patch('builtins.input', side_effect=['2', 'A', 'Ladybug'])
def test_task2_choice1_option2(mock_input, capsys):
    from task2 import main
    main()
    output = capsys.readouterr().out
    assert "2) Form the ball into an egg shape." in output


@patch('builtins.input', side_effect=['3', 'A', 'Ladybug'])
def test_task2_choice1_option3(mock_input, capsys):
    from task2 import main
    main()
    output = capsys.readouterr().out
    assert "2) Keep it round." in output


@patch('builtins.input', side_effect=['1', 'A', 'Ladybug'])
def test_task2_choice2_optionA(mock_input, capsys):
    from task2 import main
    main()
    output = capsys.readouterr().out
    assert "4) Pinch off pieces of the thin ropes to make and attach spots." in output


@patch('builtins.input', side_effect=['1', 'B', 'Ladybug'])
def test_task2_choice2_optionB(mock_input, capsys):
    from task2 import main
    main()
    output = capsys.readouterr().out
    assert "4) Use the ropes to make stripes." in output


# ==================================================================
# TASK 3 - Mouse build
# ==================================================================

@patch('builtins.input', side_effect=['long body', 'long tail'])
def test_task3_color1_is_string_in_step1(mock_input, capsys):
    from task3 import main
    main()
    output = capsys.readouterr().out
    assert "1) Roll a ball using " in output


@patch('builtins.input', side_effect=['long body', 'long tail'])
def test_task3_color1_is_string_in_step3(mock_input, capsys):
    from task3 import main
    main()
    output = capsys.readouterr().out
    assert "3) Roll a smaller ball using " in output
    assert " for the head." in output


@patch('builtins.input', side_effect=['long body', 'long tail'])
def test_task3_color1_is_string_in_step6(mock_input, capsys):
    from task3 import main
    main()
    output = capsys.readouterr().out
    assert "6) Add four small legs to the bottom using " in output


@patch('builtins.input', side_effect=['long body', 'long tail'])
def test_task3_color2_is_string_in_step5_long_tail(mock_input, capsys):
    from task3 import main
    main()
    output = capsys.readouterr().out
    assert "5) Roll a thin rope using " in output
    assert " and attach to the back." in output


@patch('builtins.input', side_effect=['long body', 'short tail'])
def test_task3_color2_is_string_in_step5_short_tail(mock_input, capsys):
    from task3 import main
    main()
    output = capsys.readouterr().out
    assert "5) Add a small bump using " in output
    assert " to the back." in output


@patch('builtins.input', side_effect=['long body', 'long tail'])
def test_task3_input1_prompt_text(mock_input, capsys):
    from task3 import main
    main()
    assert mock_input.call_args_list[0][0][0] == "long body or round body? "


@patch('builtins.input', side_effect=['long body', 'long tail'])
def test_task3_input2_prompt_text(mock_input, capsys):
    from task3 import main
    main()
    assert mock_input.call_args_list[1][0][0] == "long tail or short tail? "


@patch('builtins.input', side_effect=['long body', 'long tail'])
def test_task3_choice1_long_body(mock_input, capsys):
    from task3 import main
    main()
    output = capsys.readouterr().out
    assert "2) Roll the ball into an egg shape." in output


@patch('builtins.input', side_effect=['round body', 'long tail'])
def test_task3_choice1_round_body(mock_input, capsys):
    from task3 import main
    main()
    output = capsys.readouterr().out
    assert "2) Keep it as a ball." in output


@patch('builtins.input', side_effect=['long', 'long tail'])
def test_task3_choice1_checks_full_response_not_partial(mock_input, capsys):
    """Input 'long' should not match 'long body' - check the full response."""
    from task3 import main
    main()
    output = capsys.readouterr().out
    assert "2) Keep it as a ball." in output


@patch('builtins.input', side_effect=['long body', 'long tail'])
def test_task3_choice2_long_tail(mock_input, capsys):
    from task3 import main
    main()
    output = capsys.readouterr().out
    assert "5) Roll a thin rope using " in output


@patch('builtins.input', side_effect=['long body', 'short tail'])
def test_task3_choice2_short_tail(mock_input, capsys):
    from task3 import main
    main()
    output = capsys.readouterr().out
    assert "5) Add a small bump using " in output


@patch('builtins.input', side_effect=['long body', 'long'])
def test_task3_choice2_checks_full_response_not_partial(mock_input, capsys):
    """Input 'long' should not match 'long tail' - check the full response."""
    from task3 import main
    main()
    output = capsys.readouterr().out
    assert "5) Add a small bump using " in output


# ==================================================================
# TASK 4 - Dog build
# ==================================================================

@patch('builtins.input', side_effect=['hot dog', 'standing up'])
def test_task4_color1_is_string_in_step1(mock_input, capsys):
    from task4 import main
    main()
    output = capsys.readouterr().out
    assert "1) Roll a ball using " in output
    assert " for the body." in output


@patch('builtins.input', side_effect=['hot dog', 'standing up'])
def test_task4_color1_is_string_in_step3(mock_input, capsys):
    from task4 import main
    main()
    output = capsys.readouterr().out
    assert "3) Roll a smaller ball using " in output
    assert " for the head." in output


@patch('builtins.input', side_effect=['hot dog', 'standing up'])
def test_task4_color1_is_string_in_step6(mock_input, capsys):
    from task4 import main
    main()
    output = capsys.readouterr().out
    assert "6) Add four legs using " in output


@patch('builtins.input', side_effect=['hot dog', 'standing up'])
def test_task4_color2_is_string_in_step5_standing_up(mock_input, capsys):
    from task4 import main
    main()
    output = capsys.readouterr().out
    assert "5) Attach two pointed pieces using " in output
    assert " upright." in output


@patch('builtins.input', side_effect=['hot dog', 'flopped down'])
def test_task4_color2_is_string_in_step5_flopped_down(mock_input, capsys):
    from task4 import main
    main()
    output = capsys.readouterr().out
    assert "5) Attach two pieces using " in output
    assert " hanging downward." in output


@patch('builtins.input', side_effect=['hot dog', 'standing up'])
def test_task4_color2_is_string_in_step6(mock_input, capsys):
    from task4 import main
    main()
    output = capsys.readouterr().out
    assert ", a small tail using " in output


@patch('builtins.input', side_effect=['hot dog', 'standing up'])
def test_task4_input1_prompt_text(mock_input, capsys):
    from task4 import main
    main()
    assert mock_input.call_args_list[0][0][0] == "hot dog or round like a ball? "


@patch('builtins.input', side_effect=['hot dog', 'standing up'])
def test_task4_input2_prompt_text(mock_input, capsys):
    from task4 import main
    main()
    assert mock_input.call_args_list[1][0][0] == "standing up or flopped down? "


@patch('builtins.input', side_effect=['hot dog', 'standing up'])
def test_task4_choice1_hot_dog(mock_input, capsys):
    from task4 import main
    main()
    output = capsys.readouterr().out
    assert "2) Stretch it out." in output


@patch('builtins.input', side_effect=['round like a ball', 'standing up'])
def test_task4_choice1_round_like_a_ball(mock_input, capsys):
    from task4 import main
    main()
    output = capsys.readouterr().out
    assert "2) Keep it round." in output


@patch('builtins.input', side_effect=['hot', 'standing up'])
def test_task4_choice1_checks_full_response_not_partial(mock_input, capsys):
    """Input 'hot' should not match 'hot dog' - check the full response."""
    from task4 import main
    main()
    output = capsys.readouterr().out
    assert "2) Keep it round." in output


@patch('builtins.input', side_effect=['hot dog', 'standing up'])
def test_task4_choice2_standing_up(mock_input, capsys):
    from task4 import main
    main()
    output = capsys.readouterr().out
    assert "5) Attach two pointed pieces using " in output


@patch('builtins.input', side_effect=['hot dog', 'flopped down'])
def test_task4_choice2_flopped_down(mock_input, capsys):
    from task4 import main
    main()
    output = capsys.readouterr().out
    assert "5) Attach two pieces using " in output


@patch('builtins.input', side_effect=['hot dog', 'standing'])
def test_task4_choice2_checks_full_response_not_partial(mock_input, capsys):
    """Input 'standing' should not match 'standing up' - check the full response."""
    from task4 import main
    main()
    output = capsys.readouterr().out
    assert "5) Attach two pieces using " in output
