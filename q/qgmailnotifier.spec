%global debug_package %{nil}

Summary:	Qt GMail Notifier
Name:		qgmailnotifier
Version: 	2008.3
Release: 	7.1
License:	GPL
Group:		Productivity/Networking/Email/Utilities
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Vendor:		Evan Teran
BuildRequires:	gcc-c++, pkgconfig(QtGui)

%description
%{summary}

%prep
%setup -q

%build
qmake-qt4
make

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{makeinstall} INSTALL_ROOT=$RPM_BUILD_ROOT/usr
#install -Dp -m 0755 bin/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -Dp -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
install -Dp -m 0644 img/gmail.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Sun Aug 05 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2008.3
- Rebuild for Fedora
* Sun Feb 06 2011 Petr Vanek <petr@scribus.info> 2008.2
- suse fixes
* Wed Jul 08 2009 TI_Eugene <ti.eugene@gmail.com>
- Initial packaging
