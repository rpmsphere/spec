Summary: 	Ephoto manangement Software
Name: 		ephoto
Version: 	0.1.1.55225
Release: 	1
License: 	BSD
Group: 		Graphical desktop/Enlightenment
URL: 		http://get-e.org/
Source: 	%{name}-%{version}.tar.gz
Source1:	ephoto.desktop
Source2:	ephoto.png
BuildRequires:  desktop-file-utils
BuildRequires:  gettext-devel
BuildRequires:	ecore-devel, libelementary-devel, eio-devel, ethumb-devel, eet-devel, efreet-devel
BuildRequires:	elementary

%description
Enlightenment Ephoto

%prep
%setup -q

%build
export LDFLAGS='-leet'
./configure --enable-shared --disable-static --prefix=/usr
%__make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

mkdir -p $RPM_BUILD_ROOT%_datadir/applications
install -m 0644 %SOURCE1 $RPM_BUILD_ROOT%_datadir/applications

mkdir -p $RPM_BUILD_ROOT%_datadir/icons
install -m 0644 %SOURCE2 $RPM_BUILD_ROOT%_datadir/icons

rm -rf $RPM_BUILD_ROOT%{_libdir}/ephoto_ql.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%_bindir/ephoto
%_datadir/ephoto/themes/default/ephoto.edj
%_datadir/applications/ephoto.desktop
%_datadir/icons/ephoto.png
%{_bindir}/ephoto_ql
%{_libdir}/ephoto_ql.so

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Tue Jan 04 2011 Wei-Lun Chao <bluebat@member.fsf.org>
- Rebuild for OSSII

* Sun Dec 26 2010 Texstar <texstar at gmail.com> 20101226-1pclos2010
- update from svn

* Wed Dec 15 2010 Texstar <texstar at gmail.com> 20101215-1pclos2010
- update from svn
