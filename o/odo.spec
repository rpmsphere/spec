%global debug_package %{nil}

Summary: A port to C++ of my personal programming language
Name: odo
Version: 0.4
Release: 0.beta
License: LGPL3
Group: Development/Languages
Source: %{name}-master.zip
URL: https://github.com/louis1001/odo

%description
This is my first attempt at making a usable, personalized interpreted programming language.

%prep
%setup -q -n %{name}-master

%build
cmake .
%make_build

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}

%files 
%doc README.md LICENCE.txt
%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Mar 21 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.beta
- Rebuild for Fedora
