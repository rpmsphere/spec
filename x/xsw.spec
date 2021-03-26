Name: xsw
License: GPLv3
Group: Application/Office
Summary: A slideshow viewer
Version: 0.2.3
Release: 1
Source: http://xsw.googlecode.com/files/%{name}-%{version}.tar.gz
URL: http://code.google.com/p/xsw/
BuildRequires: SDL-devel, SDL_gfx-devel, SDL_ttf-devel , SDL_image-devel

%description
xsw is a slideshow presentation tool for all those who are frustrated
with Microsoft PowerPoint and its clones.

%prep
%setup -q

%build
%configure
%__make

%install
%__rm -rf %{buildroot}
%__make DESTDIR=%{buildroot} install

%clean
%__rm -rf %{buildroot}

%files
%doc AUTHORS TODO COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man?/%{name}.*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.3
- Rebuild for Fedora
