class Error :
        
    def count_error_crition(n) :

        """
        To count the error crition -> εs, 
        This method need the variable: n
        which means the signifigant figure.
        """
        error_crition = 0.5 * 10 ** (2 - n)

        return error_crition


    def count_approximate_percent_relative_error(current_approximation, previous_approximation) :

        """
        To count the approximate estimate percent relative error -> εa.
        This method need the variable: current and previous approximation.
        Then we have to avoid the situation about current approximation is 0,
        if current approximation is zero, then we return -999.
        """

        approximation_error = current_approximation - previous_approximation

        try :
            approximate_relative_error = (approximation_error / current_approximation)
            approximate_percent_relative_error = abs(approximate_relative_error) * 100

            return approximate_percent_relative_error
        except ZeroDivisionError:
            return -999


    def count_true_percent_relative_error(true_value, approximation) :   

        """
        To count the true percent relative error -> εt.
        This method need the variable: true value and approximation.
        Then we have to avoid the situation about true value is 0,
        if true value is zero, then we return -999.
        """
        true_error = true_value - approximation

        try :
            true_relative_error = (true_error / true_value)
            true_percent_relative_error = true_relative_error * 100

            return true_percent_relative_error
        except ZeroDivisionError :
            return -999
