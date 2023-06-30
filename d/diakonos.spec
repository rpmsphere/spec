Name:		diakonos
Summary:	A linux editor for the masses
Version:	0.9.4
Release:	3.1
License:	MIT
Group:		Applications/Editors
Source0:	https://diakonos.pist0s.ca/archives/%{name}-%{version}.tar.bz2
URL:		https://diakonos.pist0s.ca
BuildArch:	noarch
BuildRequires:	ruby
BuildRequires:	rubypick
BuildRequires:	rubygems

%description
A customizable, usable console-based text editor made it with the intention
of being easier to configure and use than emacs, more powerful than pico and
nano, and not as cryptic as vi or ex.

%prep
%setup -q
sed -i 's|1, 9|1, 8|' lib/diakonos/version.rb

%build

%install
ruby install.rb --prefix /usr --dest-dir $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/share/ruby
mv $RPM_BUILD_ROOT/usr/local/share/ruby/site_ruby/%{name}* $RPM_BUILD_ROOT/usr/share/ruby
rm -rf $RPM_BUILD_ROOT/usr/share/doc/ruby

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc CHANGELOG LICENCE README.rdoc
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/ruby/%{name}*
%{_sysconfdir}/%{name}*

%changelog
* Tue Nov 06 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.4
- Rebuilt for Fedora
