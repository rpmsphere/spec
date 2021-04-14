%define _name nit

Summary: Nit programming language
Name: nitlang
Version: 0.8git
Release: 1
License: Apache, BSD, GPL
Group: Development/Languages
#Source: https://github.com/nitlang/nit/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
Source: nit-master.zip
URL: https://github.com/nitlang/nit
BuildRequires: libunwind-devel
BuildRequires: gc-devel
BuildRequires: ccache

%description
Nit is an expressive language with a script-like syntax, a friendly type-system
and aims at elegance, simplicity and intuitiveness.

%prep
#setup -q -n %{_name}-%{version}
%setup -q -n nit-master

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -d %{buildroot}%{_bindir}
install -m755 bin/* %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1
install -m644 share/man/man1/* %{buildroot}%{_mandir}/man1
install -d %{buildroot}%{_datadir}/%{_name}
cp -a clib lib src %{buildroot}%{_datadir}/%{_name}
install -d %{buildroot}/etc/profile.d
echo "export NIT_DIR=%{_datadir}/%{_name}" > %{buildroot}/etc/profile.d/%{_name}.sh

%files 
%doc *.md Changelog LICENSE* NOTICE
%{_bindir}/%{_name}*
%{_mandir}/man1/%{_name}*.1.*
%{_datadir}/%{_name}
/etc/profile.d/%{_name}.sh

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Fri Nov 20 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8git
- Rebuilt for Fedora
