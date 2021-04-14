%undefine _debugsource_packages
Name:		gtkqq
Version:	0.1
Release:	11.1
Summary:	A Gtk QQ client
Group:		Productivity/Networking/Instant Messenger
License:	GPL-3.0+
URL:		https://github.com/kernelhcy/gtkqq
Source0:	%{name}-%{version}.tar.bz2
Patch1:		override_warnings_as_errors.patch
BuildRequires:  libpng-devel
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
BuildRequires:	glib2-devel
BuildRequires:	gtk2-devel >= 2.24.0
BuildRequires:	sqlite-devel
BuildRequires:	gstreamer1-devel
BuildRequires:	desktop-file-utils

%description
GtkQQ is a QQ client. It is written using gtk and based on the webqq protocol.

The webqq protocol is based on the HTTP. 
Visit http://web.qq.com to see it.

Maybe GtkQQ is a browser, whick can only visit http://web.qq.com.
I think there is no copyright problem, because I just write a highly custommed
broswer.

%prep
%setup -q
%patch1 -p1

%build
%configure --prefix=%{_prefix} --libdir=%{_libdir}
make %{?_smp_mflags}

%install
rm -f -r $RPM_BUILD_ROOT
%makeinstall
# buggy, not sure the purpose of it
rm -f $RPM_BUILD_ROOT/%{_bindir}/qq
# don't need these files, unless a devel package is added
rm -f $RPM_BUILD_ROOT/%{_libdir}/libwebqq.so
rm -f $RPM_BUILD_ROOT/%{_libdir}/libwebqq.la
rm -f $RPM_BUILD_ROOT/%{_libdir}/libwebqq.a

%files
%{_bindir}/gtkqq
%{_datadir}/gtkqq
%{_datadir}/applications/gtkqq.desktop
%{_datadir}/pixmaps/gtkqq.png
%{_libdir}/libwebqq.so.*

%clean
rm -f -r $RPM_BUILD_ROOT

%changelog
* Thu Mar 15 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Rebuilt for Fedora
* Mon Feb 13 2012 hillwood@linuxfans.org
- patch license to follow spdx.org standard
- remove %%clean in specfile
* Sat Jan 21 2012 i@marguerite.su
- fix warnings, fix build
* Sun Jan 15 2012 lyre@poetpalace.org
- Initial package 0.1
