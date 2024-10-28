%undefine _debugsource_packages
%global _name my_basic

Summary: Lightweight BASIC interpreter written with C from scratch
Name: mybasic
Version: 1.3rc
Release: 1
License: MIT
Group: Development/Languages
Source: %{_name}-master.zip
URL: https://github.com/paladin-t/my_basic

%description
MY-BASIC is aimed to be embeddable, extendable and portable, with retro and
modern syntax. May be used as an alternative of something like Lua.

%prep
%setup -q -n %{_name}-master

%build
%make_build

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 output/my_basic %{buildroot}%{_bindir}/%{name}

%files 
%doc *.md
%{_bindir}/%{name}

%changelog
* Sun Nov 12 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3rc
- Rebuilt for Fedora
