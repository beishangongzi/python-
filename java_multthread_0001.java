import java.util.concurrent.Callable;
import java.util.concurrent.FutureTask;

public class MultiThread implements Callable<Integer> {
    @Override
    public Integer call() throws Exception {
        add();
        return null;
    }

    public static void add(){
        long startTime = System.currentTimeMillis();
        for (double i = 0; i < 1000000000; i++) {

        }
        long endTime = System.currentTimeMillis();
        double time = (float)(endTime - startTime) / 1000;
        String s = String.format("线程id：%d 耗时：%f%n", Thread.currentThread().getId(), time);
        System.out.println(s);
    }

    public static void main(String[] args) throws InterruptedException {
        MultiThread multiThread = new MultiThread();
        FutureTask<Integer> future = new FutureTask<Integer>(multiThread);
        Thread thread1 = new Thread(future, "ss");

        MultiThread multiThread2 = new MultiThread();
        FutureTask<Integer> future2 = new FutureTask<Integer>(multiThread);
        Thread thread2 = new Thread(future2, "ss");

        MultiThread multiThread3 = new MultiThread();
        FutureTask<Integer> future3 = new FutureTask<Integer>(multiThread);
        Thread thread3 = new Thread(future3, "ss");

        long startTime = System.currentTimeMillis();
        thread1.start();
        thread2.start();
        thread3.start();
        thread1.join();
        thread2.join();
        thread3.join();
        long endTime = System.currentTimeMillis();
        double time = (float)(endTime - startTime) / 1000;
        String s = String.format("三次add函数运行完毕后：%d 耗时：%f%n", Thread.currentThread().getId(), time);
        System.out.println(s);

        System.out.println("开始运行add函数");
        add();



    }
}
