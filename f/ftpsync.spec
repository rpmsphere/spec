Name:          ftpsync
Version:       1.3.01
Release:       4.1
Summary:       A PERL script to synchronize a local directory tree and a remote FTP directory tree
Group:         Applications/Networking
URL:           http://ftpsync.sourceforge.net
Source:        http://ftpsync.sourceforge.net/ftpsync-%{version}.tar.bz2
License:       GPL
BuildRequires: perl-devel
BuildRequires: perl-libwww-perl
BuildArch:     noarch

%description
A PERL script to synchronize a local directory tree and a remote FTP directory tree.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -D -m 0755 ftpsync.pl $RPM_BUILD_ROOT%{_bindir}/ftpsync

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/ftpsync
%doc Changes COPYING README TODO

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.01
- Rebuilt for Fedora
* Sat May 30 2009 Silvan Calarco <silvan.calarco@mambasoft.it> 1.3.01-1mamba
- update to 1.3.01
* Fri Jun 20 2008 Silvan Calarco <silvan.calarco@mambasoft.it> 1.2.34-1mamba
- update to 1.2.34
* Wed Jan 31 2007 Silvan Calarco <silvan.calarco@mambasoft.it> 1.2.33-1qilnx
- package created by autospec
