%undefine _debugsource_packages

Summary:	Free software for creating, managing, and printing invoices
Name:		qfaktury
Version:	0.6.2.1
Release:	8.1
License:	GPL v3
Group:		Productivity/Office/Finance
Source0:	http://dl.sourceforge.net/qfaktury/%{name}-0.6.2_1.tar.gz
Source1:	qfaktury.desktop
Patch0:		remove_local_prefix.patch
URL:		http://qfaktury.sourceforge.net/
BuildRequires:  libpng-devel
BuildRequires:	gcc-c++ qt4-devel desktop-file-utils

%description
QFaktury is a software for creating, managing, and printing invoices.
It also maintains a database for contractor information, and a
database for product information. QFaktury was created for a Polish
financial system, but it can be useful in other countries with or
without small modifications.

%description -l pl
QFaktury to całkowicie darmowy i wszechstronny system fakturujący
pracujący pod kontrolą systemu Linux. Umożliwia on drukowanie faktur,
faktur pro forma i korekt, a także łatwe zarządzanie fakturami,
towarami i baza kontrahentów. Za pomocą programu QFaktury możliwe jest
również przygotowanie faktury w formacie PDF czy XML. System integruje
się z programem e-Przelewy.

%prep
%setup -q -n %{name}-0.6.2_1
%patch0

%build
rm -rf build
qmake-qt4
make

%install
make INSTALL_ROOT=$RPM_BUILD_ROOT install
%{__install} -D -m 644 icons/qfaktury_128.png "$RPM_BUILD_ROOT%{_datadir}/pixmaps/qfaktury.png"
%{__install} -D -m 644 %{SOURCE1} "$RPM_BUILD_ROOT%{_datadir}/applications/qfaktury.desktop"
%{__rm} "$RPM_BUILD_ROOT%{_datadir}/applications/QFaktury.desktop"

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%doc ChangeLog.txt Copyright.txt plans.txt ReadMe.txt
%{_bindir}/qfaktury
%dir %{_datadir}/qfaktury
%dir %{_datadir}/%{name}/icons
%{_datadir}/%{name}/icons/*.png
%dir %{_datadir}/%{name}/templates
%{_datadir}/%{name}/templates/style.css
%{_datadir}/applications/qfaktury.desktop
%{_datadir}/pixmaps/qfaktury.png

%changelog
* Sun Mar 04 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.2_1
- Rebuilt for Fedora
* Thu Jul 16 2009 Mariusz Fik <fisiu82@gmail.com> - 0.6.2_1
- upstream update
* Tue Feb 10 2009 Mariusz Fik <fisiu82@gmail.com> - 0.5.0
- initial package, upstream version
