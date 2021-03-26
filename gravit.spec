Name:           gravit
Version:        0.5.1
Release:        5.1
Summary:        A Gravity Simulator
License:        GPL
URL:            http://gravit.slowchop.com/
Source0:        http://gravit.slowchop.com/media/downloads/%{name}-%{version}.tar.gz
BuildRequires:  lua-devel, SDL-devel, SDL_ttf-devel, SDL_image-devel

%description
Gravit is a free, visually stunning gravity simulator, where you can spend
endless time experimenting with various configurations of simulated universes.

%prep
%setup -q

%build
export LDFLAGS=-Wl,--allow-multiple-definition
./autogen.sh
%ifarch aarch64
sed -i -e '4763,4765d' -e '4778,4780d' configure
%endif
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
%doc ChangeLog COPYING README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_sysconfdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Fri Dec 26 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.1
- Rebuild for Fedora
