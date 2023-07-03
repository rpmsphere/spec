%global srcname pyInputStats

Name:           pyinputstats
Version:        0.2.1
Release:        4.1
Summary:        An application for mouse and keyboard statistics
Group:          Applications/System
License:        GPLv2+
URL:            https://launchpad.net/pyinputstats
Source0:        https://launchpad.net/%{name}/trunk/1.0/+download/%{srcname}-%{version}.tar.gz
Source1:        %{name}.desktop
BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  desktop-file-utils
Requires:       python2-xlib

%description
pyInputStats watches your mouse and your keyboard in order to generate
some statistics. With pyInputStats you are able to answer substantial
questions like:

* How many meters do I move my mouse pointer every day?
* How many times to I press a key on my keyboard?
* Do I click my mouse more often on Fridays?
* Do I make more mouse-meters in the morning hours?

%prep
%setup -q -n %{srcname}-%{version}
# For the desktop file
cp -p pyinputstatsmodules/images/ruler.png %{name}.png
# Remove shebangs
for Files in \
    pyinputstatsmodules/{database.py,__init__.py,gui.py,collector.py,helpers.py} \
    pygtk_chart/{chart.py,__init__.py,label.py,chart_object.py,pie_chart.py,basics.py,line_chart.py} \
    ; do
  %{__sed} -i.orig -e 1d ${Files}
  touch -r ${Files}.orig ${Files}
  %{__rm} ${Files}.orig
done

%build
python2 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python2 setup.py install -O1 --skip-build --root=$RPM_BUILD_ROOT
desktop-file-install --dir=$RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
install -Dp -m 0644 %{name}.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README
%{_bindir}/%{name}
%{python2_sitelib}/pyinputstatsmodules/
%{python2_sitelib}/pygtk_chart/
%{python2_sitelib}/%{srcname}*.egg-info
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Thu Feb 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.1
- Rebuilt for Fedora
* Sat Mar 26 2011 Fabian Affolter <fabian@bernewireless.net> - 0.2.1-1
- Initial package for Fedora
