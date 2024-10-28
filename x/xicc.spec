Name:           xicc
Version:        0.2
Release:        3.1
License:        GNU General Public License (GPL)
Summary:        ICC profiles in X
URL:            https://burtonini.com/blog/computers/xicc
Group:          System/X11/Utilities
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  libX11-devel
BuildRequires:  pkgconfig(glib-2.0)

%description
ICC profiles in X

%prep
%setup -q

%build
%configure
make

%install
%makeinstall

%files
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/xicc

%changelog
* Thu Sep 22 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuilt for Fedora

* Tue Jul 10 2007 prusnak@suse.cz
- initial version (0.2)
