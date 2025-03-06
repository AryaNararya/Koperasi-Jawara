import { useState } from "react";
import { useForm } from "react-hook-form";
import { useRouter } from "next/router";

export default function AuthPage() {
  const [isRegister, setIsRegister] = useState(false);
  const { register, handleSubmit, formState: { errors } } = useForm();
  const router = useRouter();

  const onSubmit = async (data) => {
    if (isRegister) {
      console.log("Registering:", data);
    } else {
      console.log("Logging in:", data);
    }
    router.push("/dashboard");
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-[#EFEDE1]">
      <div className="bg-[#D9C3A5] p-8 rounded-lg shadow-md w-96">
        <h2 className="text-2xl font-bold text-center mb-6 text-[#2F5D3F]">
          {isRegister ? "Register" : "Login"}
        </h2>
        <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
          {isRegister && (
            <div>
              <label className="block text-sm font-medium text-[#2F5D3F]">Nama</label>
              <input {...register("name", { required: true })} className="mt-1 p-2 w-full border border-[#6BA56D] rounded-md" />
              {errors.name && <span className="text-red-500 text-sm">Nama wajib diisi</span>}
            </div>
          )}
          <div>
            <label className="block text-sm font-medium text-[#2F5D3F]">Email</label>
            <input type="email" {...register("email", { required: true })} className="mt-1 p-2 w-full border border-[#6BA56D] rounded-md" />
            {errors.email && <span className="text-red-500 text-sm">Email wajib diisi</span>}
          </div>
          <div>
            <label className="block text-sm font-medium text-[#2F5D3F]">Password</label>
            <input type="password" {...register("password", { required: true, minLength: 6 })} className="mt-1 p-2 w-full border border-[#6BA56D] rounded-md" />
            {errors.password && <span className="text-red-500 text-sm">Password minimal 6 karakter</span>}
          </div>
          <button type="submit" className="w-full bg-[#2F5D3F] text-white py-2 rounded-md hover:bg-[#6BA56D]">
            {isRegister ? "Register" : "Login"}
          </button>
        </form>
        <p className="mt-4 text-center text-sm text-[#2A4D56]">
          {isRegister ? "Sudah punya akun? " : "Belum punya akun? "}
          <button onClick={() => setIsRegister(!isRegister)} className="text-[#2F5D3F] hover:underline">
            {isRegister ? "Login" : "Register"}
          </button>
        </p>
      </div>
    </div>
  );
}
