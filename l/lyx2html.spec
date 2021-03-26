%global debug_package %{nil}

Name:          lyx2html
Version:       0.2
Release:       4.1
Summary:       A very simple Lyx to HTML converter
Group:         Graphical Desktop/Applications/Office
URL:           http://www.netmeister.org/apps/lyx2html/
Source:        http://www.netmeister.org/apps/%{name}-%{version}.tar.gz
License:       GPL

%description
A very simple Lyx to HTML converter. As the name suggests, it takes a ".lyx"
document as input and generates an HTML-file following a few simple rules.

%prep
%setup -q 
sed -i 's|-o lyx2html|-Wl,--allow-multiple-definition -o lyx2html|' Makefile

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m755 lyx2html $RPM_BUILD_ROOT%{_bindir}
install -m644 lyx2html.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc CHANGES COPYING README
%{_bindir}/lyx2html
%{_mandir}/man1/lyx2html.1*

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuild for Fedora
* Fri Oct 03 2008 Tiziana Ferro <tiziana.ferro@email.it> 0.2-2mamba
- update mantainer, vendor, distribution
- update buildrequirements list
* Tue Jan 10 2006 Alessandro Ramazzina <alessandro.ramazzina@qilinux.it> 0.2-1qilnx
- package created by autospec
