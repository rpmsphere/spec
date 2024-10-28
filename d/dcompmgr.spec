Name:           dcompmgr
Version:        0.20120403
Release:        10.1
Summary:        Alternative to xcompmgr
License:        Unknown
URL:            https://git.openbox.org/?p=dana/dcompmgr.git;a=summary
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  glib2-devel, libxcb-devel, libX11-devel, mesa-libGL-devel

%description
Alternative to xcompmgr. Used to have transparency and fade effect.

%prep
%setup -q -n %{name}
sed -i 's|-lX11-xcb|-lX11-xcb -lxcb -lxcb-xfixes -lxcb-shape -lxcb-render|' Makefile

%build
make

%install
%{__install} -D -m0755 %{name} $RPM_BUILD_ROOT/%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Tue Jul 10 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.20120403
- Rebuilt for Fedora
* Fri May 27 2011 qmp <glang@lavabit.com> - 0.20110527
- Initial packaging
