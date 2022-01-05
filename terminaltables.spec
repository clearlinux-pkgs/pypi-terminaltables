#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : terminaltables
Version  : 3.1.10
Release  : 24
URL      : https://files.pythonhosted.org/packages/f5/fc/0b73d782f5ab7feba8d007573a3773c58255f223c5940a7b7085f02153c3/terminaltables-3.1.10.tar.gz
Source0  : https://files.pythonhosted.org/packages/f5/fc/0b73d782f5ab7feba8d007573a3773c58255f223c5940a7b7085f02153c3/terminaltables-3.1.10.tar.gz
Summary  : Generate simple tables in terminals from a nested list of strings.
Group    : Development/Tools
License  : MIT
Requires: terminaltables-license = %{version}-%{release}
Requires: terminaltables-python = %{version}-%{release}
Requires: terminaltables-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(poetry)

%description
## terminaltables
# What is it
Easily draw tables in terminal/console applications from a list of lists of strings. Supports multi-line rows.

%package license
Summary: license components for the terminaltables package.
Group: Default

%description license
license components for the terminaltables package.


%package python
Summary: python components for the terminaltables package.
Group: Default
Requires: terminaltables-python3 = %{version}-%{release}

%description python
python components for the terminaltables package.


%package python3
Summary: python3 components for the terminaltables package.
Group: Default
Requires: python3-core
Provides: pypi(terminaltables)

%description python3
python3 components for the terminaltables package.


%prep
%setup -q -n terminaltables-3.1.10
cd %{_builddir}/terminaltables-3.1.10

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641424282
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/terminaltables
cp %{_builddir}/terminaltables-3.1.10/LICENSE %{buildroot}/usr/share/package-licenses/terminaltables/ce98a25c85e769d19cb57ab33b77a99c8b7e8b40
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/terminaltables/ce98a25c85e769d19cb57ab33b77a99c8b7e8b40

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
