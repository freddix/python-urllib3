%define 	module	urllib3

Summary:	HTTP library with thread-safe connection pooling, file post, and more
Name:		python-%{module}
Version:	1.7
Release:	1
License:	MIT
Group:		Development/Languages/Python
Source0:	https://pypi.python.org/packages/source/u/urllib3/%{module}-%{version}.tar.gz
# Source0-md5:	a055b7f51b0c9ffadd7172c21b2885a3
URL:		http://urllib3.readthedocs.org/
BuildRequires:	python-modules
BuildRequires:	python3-modules
BuildRequires:	rpm-pythonprov
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python HTTP module with connection pooling and file POST abilities.
Features are:
- Re-use the same socket connection for multiple requests (with
  optional client-side certificate verification).
- File posting (encode_multipart_formdata).
- Built-in redirection and retries (optional).
- Supports gzip and deflate decoding.
- Thread-safe and sanity-safe.

%package -n python3-urllib3
Summary:	HTTP library with thread-safe connection pooling, file post, and more
Group:		Development/Languages/Python
Requires:	python3-modules

%description -n python3-urllib3
Python HTTP module with connection pooling and file POST abilities.
Features are:
- Re-use the same socket connection for multiple requests (with
  optional client-side certificate verification).
- File posting (encode_multipart_formdata).
- Built-in redirection and retries (optional).
- Supports gzip and deflate decoding.
- Thread-safe and sanity-safe.

%prep
%setup -qn %{module}-%{version}

%build
%{__python} setup.py build -b python
%{__python3} setup.py build -b python3

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py build -b python install \
	--optimize=2		\
	--root=$RPM_BUILD_ROOT	\
	--skip-build

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%{__python3} setup.py build -b python3 install \
	--optimize=2		\
	--root=$RPM_BUILD_ROOT	\
	--skip-build

# dummyserver is a part of unitstests
%{__rm} -rf $RPM_BUILD_ROOT%{py_sitescriptdir}/dummyserver \
	$RPM_BUILD_ROOT%{py3_sitescriptdir}/dummyserver

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.rst CONTRIBUTORS.txt README.rst
%{py_sitescriptdir}/%{module}

%files -n python3-urllib3
%defattr(644,root,root,755)
%doc CHANGES.rst CONTRIBUTORS.txt README.rst
%{py3_sitescriptdir}/%{module}

