Name:           duc
Version:        1.4.5
Release:        1
Summary:        Collection of tools for inspecting and visualizing disk usage
License:        LGPL-3.0-only
Group:          System/Filesystems
URL:            https://github.com/zevv/duc
Source:         https://github.com/zevv/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cairo-devel
BuildRequires:  glfw-devel
BuildRequires:  ncurses-devel
BuildRequires:  pango-devel
BuildRequires:  sqlite-devel

%description
Duc is a collection of tools for inspecting and visualizing disk usage.
Duc scales quite well, it has been tested on systems with more than 500 million
files and several petabytes of storage.

%prep
%setup -q

%build
%configure --enable-opengl \
  --disable-x11 \
  --enable-cairo \
  --with-db-backend=sqlite3

make %{?_smp_mflags}

%install
%make_install

%files
%license LICENSE
%doc ChangeLog README.md
%{_bindir}/duc
%{_mandir}/man1/duc.1*

%changelog
* Sun Oct 16 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4.5
- Rebuilt for Fedora
* Mon Feb 26 2018 mvetter@suse.com
- Change license to LGPL-3
* Mon Feb 26 2018 mvetter@suse.com
- Inital package for openSUSE in version 1.4.3
