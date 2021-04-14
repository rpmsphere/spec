%undefine _debugsource_packages

Name: mtc
Version: 0.20180824
Release: 5.1
Summary: Modula-2 to C Translator
License: open source
Group: Development/Languages
URL: https://github.com/GunterMueller/MTC-Modula-2_to_C_Translator
Source0: MTC-Modula-2_to_C_Translator-master.zip

%description
This is a port of mtc, a program to convert Modula-2 to C. Main parts are:
* mtc: translates sources in Modula-2 to C, with
* makemake: creates a Makefile to translate, compile and link a source
* reuse: library of reusable modules

%prep
%setup -q -n MTC-Modula-2_to_C_Translator-master
sed -i 's| -m32||' */*/Makefile*

%build
make INST=%{_libdir}/%{name}

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_libdir}/%{name}/{makemake,lib,include,src,mtc}

sed 's;LIB;/usr/lib64/mtc;g' mtc/m2c/mtc.sh > %{buildroot}%{_bindir}/mtc
install -c -s -m 755 mtc/m2c/mtc %{buildroot}%{_libdir}/%{name}/mtc
install -c -m 644 mtc/m2c/Scanner.Tab %{buildroot}%{_libdir}/%{name}/mtc
install -c -m 644 mtc/m2c/Parser.Tab %{buildroot}%{_libdir}/%{name}/mtc
cp mtc/m2c/SYSTEM_.h mtc/m2c/SYSTEM_.c mtc/m2c/Arguments.h mtc/m2c/Arguments.c %{buildroot}%{_libdir}/%{name}/mtc
chmod +r %{buildroot}%{_libdir}/%{name}/mtc/[AES]*.[hc]

sed 's;^LIB=.*;LIB=%{_libdir}/%{name}/makemake;' mtc/make/makemake > %{buildroot}%{_bindir}/makemake
install -c -s -m 755 mtc/make/GetImports %{buildroot}%{_libdir}/%{name}/makemake
install -c -m 644 mtc/make/Scanner.Tab %{buildroot}%{_libdir}/%{name}/makemake
install -c -m 644 mtc/make/Parser.Tab %{buildroot}%{_libdir}/%{name}/makemake
install -c -m 644 mtc/make/makemake.awk %{buildroot}%{_libdir}/%{name}/makemake

install -m 644 mm_linux.awk %{buildroot}%{_libdir}/%{name}/makemake/makemake.awk
install -m 644 reuse/m2c/libreuse.a %{buildroot}%{_libdir}/%{name}/lib
install -m 644 reuse/m2c/*.h %{buildroot}%{_libdir}/%{name}/include
install -m 644 reuse/src/*.m[di] %{buildroot}%{_libdir}/%{name}/src

%files
%doc COPYRIGHT README
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/makemake
%{_libdir}/%{name}

%changelog
* Tue Oct 23 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.20180824
- Rebuilt for Fedora
