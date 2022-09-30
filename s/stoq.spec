%undefine _debugsource_packages

Summary:	A powerful retail system
Name:		stoq
Version:	7.14.0
Release:	1
License:	GPL
Group:		System/Libraries
URL:		https://github.com/stoq/stoq
#Source0:	https://github.com/stoq/stoq/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source0:	%{name}-master.zip
BuildRequires:	python3-setuptools
BuildRequires:	python3-kiwi
BuildRequires:	python3-devel
%ifarch x86_64
BuildRequires:	grub2-efi-x64
%endif
Requires:	postgresql-server >= 8.4
Requires:	postgresql-contrib >= 8.4
Requires:	pygtk2 >= 2.20
Requires:	pypoppler >= 0.12.1
Requires:	python-dateutil >= 1.4.1
Requires:	python-imaging >= 1.1.5
Requires:	python-gudev >= 147
Requires:	python-kiwi >= 1.10
Requires:	python-mako >= 0.2.5
Requires:	python-psycopg2 >= 2.0.5
Requires:	python-storm >= 0.19
Requires:	python-reportlab >= 2.4
Requires:	python-zope-interface >= 3.0.1
Requires:	stoqdrivers >= 0.9.24
Requires:	pywebkitgtk >= 1.1.7
Requires:	python-twisted-core >= 10.0.0
Requires:	python-twisted-web >= 10.0.0
Requires:	python-xlwt >= 0.7.2
Requires:	weasyprint >= 0.15
Requires:	yelp
Requires:	iso-codes >= 3.12
BuildArch:	noarch

%description
Stoq is a suite of Retail Management System applications.
It includes the following applications;
Point of Sales, Cash register, Sales, Purchase Orders, Inventory control,
Customer Relationship Management (CRM), Financial Accounting,
Accounts Payable and Accounts Receivable, Printable Reports, 
Employees and Suppliers registry.

%prep
%setup -q -n %{name}-master

%build
python3 setup_old.py build

%install
mkdir -p %{_etcdir}/stoq
rm -rf %{buildroot}
python3 setup_old.py install -O1 --skip-build --root %{buildroot}
rm -rf %{buildroot}%{_defaultdocdir}
rm %{buildroot}%{python3_sitelib}/stoq-%{version}-py2.7.egg-info/requires.txt
%find_lang %{name}

sed -i 's|/usr/bin/python$|/usr/bin/python3|' %{buildroot}%{_bindir}/*

%files -f %{name}.lang
%doc AUTHORS CONTRIBUTORS COPYING README NEWS
%doc %{_datadir}/stoq/docs/*
%{_bindir}/stoq
%{_bindir}/stoqdbadmin
%{_datadir}/stoq/scripts/createdbuser.sh
%{_datadir}/stoq/plugins
%{python3_sitelib}/*.egg-info
%{_datadir}/icons/hicolor/48x48/apps/stoq.png
%{_datadir}/polkit-1/actions/br.com.stoq.createdatabase.policy
%{_datadir}/stoq/csv
%{_datadir}/stoq/glade
%{_datadir}/stoq/html
%{_datadir}/stoq/misc
%{_datadir}/stoq/pixmaps
%{_datadir}/stoq/sql
%{_datadir}/stoq/template
%{_datadir}/stoq/uixml
%{_datadir}/stoq/scripts/packageinstaller.py*
%{_datadir}/applications/stoq.desktop
%{_datadir}/gnome/help
%{python3_sitelib}/stoq
%{python3_sitelib}/stoqlib

%changelog
* Sun Sep 18 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 7.14.0
- Rebuilt for Fedora
* Fri Feb 17 2017 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1.11.3-3
- (e65da9f) MassBuild#1257: Increase release tag
