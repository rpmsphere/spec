#global debug_package %{nil}

Summary: A programming language for the ancient Chinese
Name: wenyan
Version: 0.3.4
Release: 1
License: MIT
Group: Development/Languages
Source: https://github.com/wenyan-lang/wenyan/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
URL: https://github.com/wenyan-lang/wenyan/
BuildRequires: nodejs

%description
Wenyan is an esoteric programming language that closely follows the grammar
and tone of classical Chinese literature.

%prep
%setup -q

%build
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files 
%doc LICENSE *.md
%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Mar 21 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.4
- Rebuild for Fedora
