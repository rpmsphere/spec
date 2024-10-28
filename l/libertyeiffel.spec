Name:           libertyeiffel
Version:        2016.05
Release:        7.1
Summary:        The GNU Eiffel Compiler and Libraries
Group:          Development/Languages
License:        GPLv2+
URL:            https://www.liberty-eiffel.org/
Source0:        https://download.savannah.gnu.org/releases/liberty-eiffel/bell.tar.gz
BuildRequires:  libX11-devel
Obsoletes:      smarteiffel

%description
It is a free eiffel compiler started from SmartEiffel code base. Its goal is
to retain its predecessor's rigour, but not its rigidity.
Think of Liberty Eiffel as SE liberated from its academic constraints.

%undefine _debugsource_packages

%prep
%setup -q -n bell
sed -i -e 's|/usr/local|%{buildroot}/usr|' -e 's|/usr/etc|/etc|' install.sh

%build
%configure
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install
echo "./" >> %{buildroot}%{_datadir}/liberty-eiffel/src/liberty_staging/loadpath.se

%files
%doc AUTHORS COPYING PATTERNS.txt README.md
%{_bindir}/se
%{_datadir}/liberty-eiffel
%{_datadir}/emacs/site-lisp/liberty-eiffel
/usr/lib/liberty-eiffel
/etc/xdg/liberty-eiffel

%changelog
* Fri Sep 21 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2016.05
- Rebuilt for Fedora
