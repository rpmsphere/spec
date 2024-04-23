%undefine _debugsource_packages

Name:           leo
Version:        6.7.7
Release:        1
Summary:        Leonine Editor with Outlines
URL:            https://webpages.charter.net/edreamleo/front.html
License:        MIT
Group:          Applications/Editor
Source0:	leo-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3
BuildRequires:  python3-setuptools

%description
Leo is a power tool for people who want to organize, study and work with data,
especially complex data like computer programs, books, web sites and data bases.
Superficially, Leo may look like other outlining programs, code folding editors
or class browsers, but it most certainly is not.

%prep
%setup -q

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_datadir}/applications
cat << EOF > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Version=1.0
Encoding=UTF-8
Name=Leo
Comment=Leonine Editor with Outlines
Exec=%{name}
Icon=%{python3_sitelib}/%{name}/Icons/leoapp32.png
Terminal=false
Type=Application
StartupNotify=true
Categories=Utility;TextEditor;
EOF

sed -i 's|/usr/bin/python$|/usr/bin/python4|' %{buildroot}%{python3_sitelib}/leo/external/saveleo \
       %{buildroot}%{python3_sitelib}/leo/plugins/leo_babel/examples/slowOut.py \
       %{buildroot}%{python3_sitelib}/leo/plugins/leo_babel/examples/slowOutNoFlush.py
#sed -i 's|/usr/bin/python.*|/usr/bin/python2|' %{buildroot}%{_bindir}/* %{buildroot}%{python2_sitelib}/leo/external/saveleo
#sed -i 's|/usr/bin/env python.*|/usr/bin/python2|' %{buildroot}%{_bindir}/* %{buildroot}%{python2_sitelib}/leo/scripts/leo

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc *.TXT
%{_bindir}/%{name}*
%{_datadir}/applications/%{name}.desktop
%{python3_sitelib}/%{name}*

%changelog
* Sun Apr 07 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 6.7.7
- Rebuilt for Fedora
