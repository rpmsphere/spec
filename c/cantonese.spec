%global _name Cantonese

Summary: The Cantonese programming language
Name: cantonese
Version: 1.0.1
Release: 1
License: MIT
Group: Development/Languages
Source0: %{_name}-main.zip
URL: https://github.com/StepfenShawn/Cantonese
BuildRequires: python3-wheel
BuildArch: noarch

%description
It is a programming language that communicates with computers in Cantonese.
The computer can read the Cantonese you write and you can operate (abuse)
the computer in Cantonese.

%prep
%setup -q -n %{_name}-main
sed -i 's|tk = kw_then|tk = [kw_then, tr_kw_then]|' src/cantonese.py

%build
%py3_build

%install
%py3_install
if [ -f %{buildroot}%{python3_sitelib}/src/'#U6fd1#U5622.py' ] ; then
  mv %{buildroot}%{python3_sitelib}/src/'#U6fd1#U5622.py' %{buildroot}%{python3_sitelib}/src/'濑嘢.py'
fi

%files 
%doc LICENSE *.md
%{_bindir}/*
%{python3_sitelib}/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Oct 02 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.1
- Rebuilt for Fedora
