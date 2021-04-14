Summary: 	X Address Translation
Name:		xat
Version: 	0.1.0
Release: 	1
License: 	GPLv2
Group: 		User Interface/X
URL: 		http://wiki.c3sl.ufpr.br/multiseat/index.php/Xat
Source0: 	%{name}-%{version}.tar.gz
BuildRequires:  libXi-devel, libX11-devel

%description
Xat is an application that serves as an intermediary between the X clients and
a multiheaded X server. Xat deceives its clients who have the impression  that
the server has only one head. The objective is that each head behaves, of  the
client's point of view, as a separate X server.  We  can  imagine  a  scenario
where we have a xserver on display :1 with four screens (:1.0, :1.1, :1.2  and
:1.3). After Xat being connected we have four displays (:2, :3, :4 and :5) and
just one screen per display. This makes multiseat viable if we  introduce  the
Multi-Pointer X server (MPX) to take care of all input devices.

%prep
%setup -q

%build
./autogen.sh --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS README
%{_bindir}/%{name}

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.0
- Rebuilt for Fedora
