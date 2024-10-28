Summary: Reverse Polish calculator / scripting language
Name: laskin
Version: 1.0.0git
Release: 1
License: BSD
Group: Development/Language
Source0: https://github.com/RauliL/laskin/archive/refs/heads/master.zip#/%{name}-master.zip
URL: https://github.com/RauliL/laskin
BuildRequires: unzip cmake

%description
Laskin is a reverse polish notation calculator / programming language inspired by Forth, RPL and Plorth.

%prep
%setup -q -n %{name}-master
sed -i '268i static void w_write(class context& context, std::ostream& out) {out << context.pop() << std::flush;}' common/src/api/utils.cpp
sed -i '469i { U"..", w_write },' common/src/api/utils.cpp

%build
%{cmake}
%{cmake_build}

%install
%{cmake_install}

%files
%doc LICENSE README.md
%{_bindir}/%{name}

%changelog
* Thu Sep 19 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.0git
- Rebuilt for Fedora
