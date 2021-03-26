%global debug_package %{nil}

Name: mumpsc
Summary: Mumps Interpreter / Compiler
Version: 20.06
Release: 1
Group: Development/Languages
License: GPLv2
URL: https://www.cs.uni.edu/~okane/
Source0: http://www.cs.uni.edu/~okane/source/MUMPS-MDH/mumps-%{version}.src.tar.gz
BuildRequires: pcre-devel
Recommends: astyle

%description
Mumps (also referred to as M) is a general purpose programming language that
supports a unique, hierarchical (or multidimensional) database facility.
It was originally developed in the late 1960s and the acronym stands for the
Massachusetts General Hospital Utility Multi-programming System. It was
(and is) widely used in clinical computing. Its original purpose was to store
tree structured medical records.

%prep
%setup -q -n %{name}

%build
%configure
sed -i 's|-o mumps2c|-Wl,--allow-multiple-definition -o mumps2c|' Makefile
make clean
make %{?_smp_mflags}

%install
sed -i 's|-pipe|-pipe -fPIE|' mumpsc
rm mumps
make -i install PREFIX=%{buildroot}/usr

if ! [ -f mumps ]; then
g++ -O3 -w -Iinclude -D_MDH_ \
%ifarch x86_64 aarch64
-L/usr/lib64 -D_FILE_OFFSET_BITS=64 \
%else
-L/usr/lib -D_FILE_OFFSET_BITS=32 \
%endif
-L. -D_LARGEFILE_SOURCE -o mumps ./mumps.cpp -lm -lmumps -lmpscpp -lmumps -lmpsglobal_native -lpcre -fpermissive -lgmp -lreadline -lmpfr
install -Dm755 mumps %{buildroot}%{_bindir}/mumps
fi

mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_mandir}/*.1 %{buildroot}%{_mandir}/man1
%ifarch x86_64 aarch64
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
#sed -i 's|/lib|/lib64|' %{buildroot}%{_bindir}/mumpsc
%endif
#rm %{buildroot}%{_bindir}/*.bat
rm -rf %{buildroot}%{_datadir}/Doc

%files
%doc README.* Licenses Doc/*.pdf
%{_bindir}/*
%{_mandir}/man1/*.1.*
%{_includedir}/*
%{_libdir}/lib*.a

%changelog
* Thu Jul 30 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 20.06
- Rebuild for Fedora
* Sat Dec 16 2003 Spec File 
- No Changes yet !! Because this is Release 1
