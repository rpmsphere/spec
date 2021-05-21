Name:           grandpa
Version:        0.1
Release:        1
License:        GPL
Source0:        %{name}.tar.gz
Vendor:         Fred Chien
URL:            http://code.google.com/p/grandpa/
Group:          User Interface/Desktops
Summary:        OpenGL Window Manager for Mandice Flat OS
BuildRequires:  clutter-devel, libXcomposite-devel, mesa-libGL-devel

%description
This is an OpenGL Window Manager for Mandice Flat OS, which aims to provide
an easy-use user interface for Mobile Device(Tablet, TV...etc) and specific
purpose embedded system.

At first Grandpa is a internal business project of Mandice, it was designed
and used on products for customer. Currently, we take off all commercial
parts to make it be an open source project.

For demonstration, it almost makes the same behavior that Apple iOS has.

%prep
%setup -q -n %{name}
sed -i '/clutter_stage_set_no_clear_hint/d' src/clutter-backend.c

%build
./autogen.sh
autoreconf -ifv
%configure --prefix=/usr
%{__make}

%install
%{__make} DESTDIR=%{buildroot} install

%clean
%__rm -rf %{buildroot}

%files
%{_bindir}/%{name}

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Mon Aug 22 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1-1.ossii
- initial package
