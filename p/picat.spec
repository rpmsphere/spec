%undefine _debugsource_packages

Summary: A simple logic-based multi-paradigm programming language
Name: picat
Version: 30.6
Release: 1
License: MPL 2.0
Group: Development/Languages
Source: http://picat-lang.org/download/%{name}30_6_src.tar.gz
URL: http://picat-lang.org/

%description
Picat is a simple, and yet powerful, logic-based multi-paradigm programming
language aimed for general-purpose applications.

%prep
%setup -q -n Picat

%build
make -C emu -f Makefile.linux64

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 emu/%{name} %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{_datadir}/%{name}
cp -a exs lib %{buildroot}%{_datadir}/%{name}

%files 
%doc LICENSE README doc/*.pdf
%{_bindir}/%{name}
%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Mar 21 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 30.6
- Rebuilt for Fedora
