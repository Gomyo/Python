SELECT STAGE, ROUND(AVG(STUDENT_NUM),0),ROUND(SUM(STUDENT_NUM)/SUM(TEACHER_NUM),1) FROM SCHOOLS
GROUP BY STAGE ORDER BY ROUND(AVG(STUDENT_NUM),0) DESC 

