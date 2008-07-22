%define pkgname pyspi

Summary: Python binding for AT-SPI
Name: python-spi
Version: 0.5.4
Release: %mkrel 2
License: GPL
Group: Development/Python
URL: http://people.redhat.com/zcerza/dogtail/
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{pkgname}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: python-devel
BuildRequires: pyrex
BuildRequires: libat-spi-devel

Provides: pyspi

%description
Python binding for AT-SPI

%prep
%setup -q -n %{pkgname}-%{version}

%build
python ./setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python ./setup.py install -O2 --root=$RPM_BUILD_ROOT 

%clean
rm -rf $RPM_BUILD_ROOT


%files 
%defattr(-,root,root,-)
%doc COPYING 
%{_libdir}/python*/site-packages/*.so

