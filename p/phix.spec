%undefine _missing_build_ids_terminate_build
%undefine _debugsource_packages

Summary: Pete's Self Hosted Hybrid Interpreter/Compiler
Name: phix
Version: 1.0.2
Release: 1
License: OSL-3.0
Group: Development/Languages
Source0: %{name}-%{version}.zip
Source1: http://phix.x10.mx/p64
URL: http://phix.x10.mx/
#BuildRequires: phix

%description
Phix is a self-hosted hybrid interpreter/compiler, developed by Pete Lomax.
It is very easy to use, and similar to Euphoria. Aims:
* Create an easy to use programming language which is also easy to modify and maintain.
* Bug location must be made as easy as possible.
* Allow the programmer to focus on solving the problem, rather than solving the solution.
* Terse may at first seem nice, but properly readable and easy to understand code is better.
    
%prep
%setup -q -n %{name}

%build
install -m755 %{SOURCE1} phix
./phix -c p
#phix -test

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 p %{buildroot}%{_bindir}/%{name}

%files 
%doc *.txt
%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun May 21 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.2
- Rebuilt for Fedora
