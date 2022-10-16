%undefine _debugsource_packages

Summary: A tiny and fast embedded scripting language
Name: pawn
Version: 4.0.6131
Release: 1
License: Apache 2.0
Group: Development/Languages
#Source: https://www.compuphase.com/%{name}/%{name}-%{version}.zip
Source: %{name}-master.zip
URL: https://www.compuphase.com/pawn/pawn.htm

%description
pawn is a simple, typeless, 32-bit extension language with a C-like syntax.
A pawn "source" program is compiled to a binary file for optimal execution
speed. The pawn compiler outputs P-code (or bytecode) that subsequently runs
on an abstract machine. Execution speed, stability, simplicity and a small
footprint were essential design criteria for both the language and the
abstract machine.

%prep
%setup -q -n %{name}-master
sed -i 's|/opt/Pawn|/usr|' compiler/sc1.c
sed -i 's|path,"include"|path,"include/%{name}"|' compiler/sc1.c

%build
export CFLAGS=-fPIE
%cmake .
%cmake_build

%install
#cmake_install
install -d %{buildroot}%{_bindir}
install -m755 *-linux-build/%{name}* *-linux-build/stategraph %{buildroot}%{_bindir}
install -d %{buildroot}%{_includedir}/%{name}
install -m644 include/* %{buildroot}%{_includedir}/%{name}

%files 
%doc LICENSE NOTICE history.txt readme.txt
%{_bindir}/*
%{_includedir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Oct 02 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 4.0.6131
- Rebuilt for Fedora
