%undefine _debugsource_packages

Summary: A pratical stack language
Name: factor
Version: 0.98
Release: 11.1
License: BSD
Group: Development/Languages
Source: http://downloads.factorcode.org/releases/%{version}/%{name}-src-%{version}.zip
URL: https://factorcode.org/
BuildRequires: gtkglext-devel

%description
Factor is a concatenative, stack-based programming language with high-level
features including dynamic types, extensible syntax, macros, and garbage
collection.

%prep
%setup -q -n %{name}

%build
%ifarch aarch64
sed -i '/-m64/d' vm/Config.x86.64
%make_build linux-x86-64
%else
%make_build
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}-ui

%files 
%doc README.md LICENSE.txt
%{_bindir}/%{name}-ui

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Aug 28 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.98
- Rebuilt for Fedora
