#undefine _debugsource_packages

Summary: The Smart Contract Programming Language
Name: solidity
Version: 0.8.17
Release: 1
License: GPL3.0+
Group: Development/Languages
Source: https://github.com/ethereum/solidity/releases/download/v%{version}/%{name}_%{version}.tar.gz
URL: https://github.com/ethereum/solidity

%description
Solidity is a statically-typed curly-braces programming language designed
for developing smart contracts that run on the Ethereum Virtual Machine.
Smart contracts are programs that are executed inside a peer-to-peer network
where nobody has special authority over the execution, and thus they allow
anyone to implement tokens of value, ownership, voting, and other kinds of logic.

%prep
%setup -q -n %{name}_%{version}
#sed -i 's|/opt/Pawn|/usr|' compiler/sc1.c
#sed -i 's|path,"include"|path,"include/%{name}"|' compiler/sc1.c

%build
#export CFLAGS=-fPIE
%cmake .
%cmake_build

%install
%cmake_install
#install -d %{buildroot}%{_bindir}
#install -m755 *-linux-build/%{name}* *-linux-build/stategraph %{buildroot}%{_bindir}
#install -d %{buildroot}%{_includedir}/%{name}
#install -m644 include/* %{buildroot}%{_includedir}/%{name}

%files 
%doc LICENSE.txt *.md
#{_bindir}/*
#{_includedir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Oct 02 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.17
- Rebuilt for Fedora
