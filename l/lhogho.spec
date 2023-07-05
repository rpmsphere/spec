%undefine _debugsource_packages

Name:		lhogho
Version:	0.0.027
Release:	25.1
Summary:	The Real Logo Compiler
Group:		Development/Languages
License:	GPL
Source0:	https://sourceforge.net/projects/lhogho/files/%{name}/%{version}/%{name}.%{version}.src.tar.gz
Source1:	_runtime.h
URL:		https://lhogho.sourceforge.net/
Patch:		lhogho-0.0.026-64bit.patch

%description
Lhogho is a free version of the programming language Logo and a promoter of its
educational philosophy. It is specially designed to be performant, miniature,
open-minded and ... artistic.

%prep
%setup -q -c
echo %{version} > src/version
echo 'OS=Linux' > src/MakefileOS
%ifarch x86_64
echo 'PROCESSOR=x86_64' >> src/MakefileOS
%else
%ifarch aarch64
echo 'PROCESSOR=aarch64' >> src/MakefileOS
%else
echo 'PROCESSOR=x86' >> src/MakefileOS
%endif
%endif
%patch -p1

%ifarch %ix86
sed -i 's/runtime\.h/_runtime.h/' src/core/runtime.c
sed -i '/rt_closeall()/d' src/core/runtime.c
cp %{SOURCE1} src/core/_runtime.h
%endif

%build
cd src/core;make;cd ../..

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 src/core/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc src/doc/usr/README.TXT src/doc/usr/Lhogho.doc
%{_bindir}/*

%changelog
* Tue Apr 10 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.027
- Rebuilt for Fedora
